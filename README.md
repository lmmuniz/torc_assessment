Problem Statement:
------------------

You are provided with a nested JSON file that contains customer purchase details. The JSON contains an array of products for each customer along with details such as product name and price.

Your task is to flatten the JSON structure and extract the relevant fields: customer\_id, order\_id, product\_name, and product\_price. You will need to explode the array of products so that each product becomes a separate row.

After flattening and exploding the data, use display(df) to show the final DataFrame.

Details about JSON data source in Spark can be found [here](https://spark.apache.org/docs/3.5.2/sql-data-sources-json.html).

Input:
------

*   **File Path**: /datasets/orders.json

*   **Schema**:
    *   customer\_id (String)
    *   order\_id (String)
    *   products (Array of Structs)
        *   product\_name (String)
        *   product\_price (Integer)
            
Output:
-------

*   **Schema**:
    *   customer\_id (String)
    *   order\_id (String)
    *   product\_name (String)
    *   product\_price (Integer)
        

**Example Output**:

**customer\_idorder\_idproduct\_nameproduct\_price**C001O1001Laptop1500C001O1001Mouse25C002O1002Keyboard75

### Explanation:

*   The input JSON is nested, with each customer having multiple products in an array.
    
*   The task requires you to explode this array, flattening the nested structure so that each product corresponds to a separate row.
    
*   The output contains four columns: customer\_id, order\_id, product\_name, and product\_price.
    

### Files:

*   **Input**: /datasets/orders.json (in JSON format)
    
*   **Output**: Use display(df) to show the final DataFrame.
    

### Tip:

Look into multiline json files if you're having trouble reading the json file!
