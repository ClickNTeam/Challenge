# My Solution

    my solution i taken the data and department according to stores each store in file json with its name and sorted by id.
    then i build 6 function to serarch into files and i run it in same time with threads

# ClickN Challenge

ClickN Challenge for matching algorithm

## Challenge Description

We have a json file that contain products from different sources
The items have the same field structure as follows:

```
{
    "_id", // id for the item: type ObjectId
    "store", // contains store name: type string
    "category", // contains category of said item : type string
    "brand", // contains item brand: type string
    "name", // contains product name: type string
    "description", // contains description of the product: type string
    "image", // contains a link to the image of the product: type string
    "measurement", // contains the measurement of the product: type string
    "price", // contains the price of the product: type double
}
```

We want a function that would take the id of a product and return a list of the other items in the json file that describe the same product

```
find_item_list(string item_id):
return(list)
```

## Rewards

1. Cash prize of $100
2. Chance to join our startup team

## Submission Requirements

1. Implementation of the solution. (Preferably in Python but not mandatory)
2. Documentation on dependencies and how to build your solution (e.g. Makefile, shell scripts, requirements.txt files)
3. Include a separate descriptive file as a writeup of how you approached solving the challenge. (Preferably as PDF)
4. Submissions are done via branches based on main branch. Use relevant github account names to easily identify the person.

## Criteria for challenge submission

1. Challenge will have a deadline of 1 week. (Final submissions date: November 3rd 2022)
2. Challenge should make use of parsed_data.json file provided. First make sure to extract the parsed_data.7z to get the json file
3. Challenge should meet challenge guidelines and requirements stated above.
