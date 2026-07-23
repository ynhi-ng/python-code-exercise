"""------------------------------------------------------------------------------------------------
SALES REPORTS WITH DEPARTMENT
This program will generate sale report by checking if the sales is valid, 
then will generate a sale report including department, item type, unit sold, sale made, error and average income, with the values gotten from the price dict and sale list.
Also, it will apply price updates or item additions from a patch dictionary to a base price list.
------------------------------------------------------------------------------------------------"""

TOLERANCE = 0.001
def is_valid_sale(price:dict, item_type:str, item_quantity:int, sale_total:float)-> bool:
    """
    The function accept a dictionary contain supermarket price for all items, item type, quantity and check if the sale is valid 
    Parameter: 
    price : dictionary with key : str and value : float
    item_type : str : something that supermarket carries
    item_quantity: int : units sold
    sale_total : float : calculated charged for the sold units
    Return :
    Bool

    """

    #Initiate a variable to store bool value, return true if the sale is valid
    is_valid = False

    #If the item is already in the price dict -> calculate total and return valid is True    
    if item_type in price:
        total = price[item_type] * item_quantity
        is_valid = abs(total - sale_total) < TOLERANCE
            
    return is_valid

def flag_invalid_sales(price:dict, sales:list)-> list:

    """
    The function will accept a dictionary contain supermarket price for all items and check all sales which are invalid as per the rules of function is_valid_sale
    Parameter:
    price: dictionary with key : str and value : float
    sales : list 
    Return: 
    list of invalid sale 
    """

    #Initiate an empty list of invalid sale 
    invalid_sale_ls = []

    #Iterate through sales record and check if the sale is valid (calling is_valid_sale function)
    for sale in sales:
        item_type = sale[0]
        item_quantity = sale[1]
        sale_total = sale[2]

        #If the sale is not valid , create a copy of the invalid sale list to preserve the original sale list
        if not is_valid_sale(price,item_type,item_quantity,sale_total):
            invalid_sale_ls.append(sale[:])
    return invalid_sale_ls
    

def generate_sales_report(price:dict, sales:list)-> dict:

    """
    The function will accept a dictionary contain supermarket price for all items and will generate a dictionary summarising the day's business by item
    Parameter:
    price: dict
    sales : list
    Return
    dictionary of all sales 
    """
    #Initiate a report_temp empty dict and store each attribute equals to 0 as default value first
    report_temp = {}
    for item in price:
        report_temp[item] = {
            'units_sold': 0,
            'sales_made': 0,
            'total_sale': 0,
            'errors': 0,
            'valid_sale_count': 0
        }
    
    #Loop through each of the sale and get the value from the sales list
    for sale in sales:
        item_type = sale[0]
        item_quantity = sale[1]
        sale_total = sale[2]
        
        #If this is a new item type, add it into the report temp
        if item_type not in report_temp:
            report_temp[item_type] = {
                'units_sold': 0,
                'sales_made': 0,
                'total_sale': 0,
                'errors': 0,
                'valid_sale_count':0
            }
        
        #After each loop, update the sales made attribute to increase 1 
        report_temp[item_type]['sales_made'] += 1
        
        #Check if the sale is valid, if valid then update the value to report temp dict
        if is_valid_sale(price, item_type, item_quantity, sale_total):
            report_temp[item_type]['units_sold'] += item_quantity
            report_temp[item_type]['total_sale'] += sale_total
            report_temp[item_type]['valid_sale_count'] +=1
        else:
            report_temp[item_type]['errors'] += 1
    
    #Convert the report format to tuples
    final_report = {}
    for item in report_temp:
        units_sold = report_temp[item]['units_sold']
        sales_made = report_temp[item]['sales_made']
        errors = report_temp[item]['errors']
        
        #Calculate average sale per sale count if the sale is valid
        if  report_temp[item]['valid_sale_count']> 0:
            average_sale = report_temp[item]['total_sale'] / report_temp[item]['valid_sale_count']
        else:
            average_sale = 0
        
        #Store as a tuple in the format (units_sold, sales_made, average_sale, errors)
        final_report[item] = (units_sold, sales_made, average_sale, errors)
    
    return final_report


def patch_item_price(price:dict, patch:dict)->dict:
    """
    The function will accept a dictionary contain supermarket price for all items and a patch dictionary with latest updates
    Parameter: 
    price : dictionary with key : str and value : float
    patch : dictionary with key : str and value : float
    Return :
    dictionary produced by overlaying the patch dict onto the standard prices and items
    """
    #Initiate a copy of original price dict to preserve the original price dict
    patch_price_dict = price.copy()

    patch_price_dict.update(patch)

    return patch_price_dict

def generate_sales_reports(price:dict, patch:dict, sales:list)->list:
    """
    The function will accept a dictionary contain supermarket price for all items and a patch dictionary with latest updates and a list of sales 
    Parameter :
    price : dictionary with key : str and value : float
    patch : dictionary with key : str and value : float
    sales : list including department which made the sales
    Return :
    list 
    """
    
    #Initate an empty dictionary with department name as key and value is the list of sales record
    dept_sales = {}

    #Loop through each sales and get value from the sale list 
    for sale in sales:
        dept_name = sale[0]
        item_type = sale[1]
        item_quantity = sale[2]
        total_sale = sale[3]

        #If the department name does not exist, add an empty record
        if dept_name not in dept_sales:
            dept_sales[dept_name] = []

        dept_sales[dept_name].append([item_type,item_quantity,total_sale])
    
    #Initiate an empty report list to store the sales for each department
    reports = []

    #Loop through the key and value in dept sales dict to get the get the price
    for dept_name, dept_sale in dept_sales.items():
        dept_price = price #assign price dict to dept price as default
        
        #Check if the dept name is in the patch, if it's in patch, call function patch_item_price to update the item and price 
        if dept_name in patch:
            dept_price = patch_item_price(price,patch[dept_name])

        #Call function generate_sales_report previously to generate sale report format 
        sales_reports = generate_sales_report(dept_price, dept_sale)

        #Call function flag_invalid_sales to get the invalid sale list
        invalid_sale = flag_invalid_sales(dept_price, dept_sale)

        # Append the result in a tuple to reports list    
        reports.append((dept_name,sales_reports,invalid_sale))
    
    return reports

# TEST 

if __name__ == "__main__":
    price = {"apple": 2.0, "orange": 3.0, "tangerine": 4.0}
    patch = {
            "dep2": {"carrot": 2.5}
        }
    sales = [
            ["dep1","apple", 1, 2.0],
            ["dep1","apple", 3, 6.0],
            ["dep1","orange", 1, 2.0],
            ["dep1","carrot", 1, 8.0],
            ["dep2","orange", 3, 9.0],
            ["dep2","carrot", 2, 5.0],
            ["dep2","apricot", 1, 9.0],
            ["dep3","apricot", 1, 9.0],
        ]

    print("SALES REPORTS")
    for report in generate_sales_reports(price,patch,sales):
        print(report)