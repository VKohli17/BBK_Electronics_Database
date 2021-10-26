Links to the demo video: 

https://iiitaphyd-my.sharepoint.com/:v:/g/personal/vanshpreet_k_research_iiit_ac_in/EQUpm49sePBGg3KACrQH5WoBRF1oB-tweNy-mZjbnlLe7Q?e=irEzyb (1x speed; 10 mins)

https://iiitaphyd-my.sharepoint.com/:v:/g/personal/vanshpreet_k_research_iiit_ac_in/EQtG-Hpgt3lJkuD-3G7jmekBQn0EgRFkiJ9QFBLW_HGZXA?e=gDw5p3 (2x speed; 5 mins)

We go sequentially from researcher to administrator, and then to customer.
One (non-exhaustive) example of each query function has been highlighted in italics.

For the **researcher**, we have the option to show stats of: 

 - products
 - employees    
 - finances

For products, we can filter by product type, or not filter at all:

First enter `show products`.     *(Selection)*

 - Then, the TUI prompts you to choose product type. Here, we can choose "all" to show all products, or one of the types *(projection)* 
 - note that here fuzzy searching works, so (say) "smar" will show all products corresponding to "smartphone".
 - Next, the TUI prompts you to choose a brand. Like before, "all" and fuzzy searching are available.
 - Finally, you are prompted to choose what attribute to order the products by. 

In the demo video, we do this 4 times. Once to show all, once to show all Oppo products, once to show smartphones and once we exhibit the fuzzy searching by using "opp" instead of "oppo" and "sm" instead of "smartphone".

Similarly, for employees, we enter `show employees`. Here, we don't have any filters because there aren't any meaningful segregation criteria.

 - the TUI asks you to choose an attribute to order the employees by.
 - it also returns sum and average values of salary given out, holidays taken and hours spent at work. *(aggregate)*

We run this twice to show different filters.

Then again, for finances, we enter `show finances`. Again, no filters - we just order by different metrics. We run it twice to show that the order works.

We can then exit from the researcher login.

For the **administrator**, we can show info, update info, add info and delete info (delete data/fire employee).

`Show info` is functionally essentially the same as the one for the researcher, so we skip it. 

For `update info`, we can update employee credentials or product info. *(modification)*

 - First we update employee credentials.
 - Then we update product info.

For `add info` we can add new employees or products.

 - First we add a new employee.
 - Then we add a new product.

For `delete info`, we can delete an employee or a product.          *(deletion)*

 - First we delete an employee.
 - Then we delete a product.

The "back page" just leads us back to the previous page.

For a **customer**, we can create a new customer account, and the script asks us to enter credentials. This has been demonstrated in the video.

After that, we can login through a customer's account and then:

 - buy a device (buying it also increments its "sales" in the product table by one. Also, fuzzy search works and asks you which of the results you want to buy)
 - show our devices
 - show all devices 
 - add a review
 - edit review
 - show our reviews
 - show all reviews for a product (fuzzy search for product works)
 - delete review
 - return device
 - edit our account
 - delete our account
 - logout (takes us back to the previous page)