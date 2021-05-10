# Profitable_Japanese_Restaurant
The goal is to acquire data through webscraping to find out the best way to open a Japanese restaurant on HK Island, by choosing the best price range, cuisine and location.
![image](https://user-images.githubusercontent.com/80243823/117673469-67a9c480-b1dd-11eb-8c7d-b8f7ee6ba48e.png)

## **Data Collection**
We use Openrice as our source of data and acquire its data through webscraping
![image](https://user-images.githubusercontent.com/80243823/117673764-a50e5200-b1dd-11eb-9f5b-f631a8b222d2.png)

We target 7 types of data to acquire. By specifying the html elements or CSS classes, we are able to pinpoint which part of the website belongs to which type of data
![image](https://user-images.githubusercontent.com/80243823/117673996-e3a40c80-b1dd-11eb-9863-ec06dcdca356.png)

However, we realise Openrice limits the number of result per search to 250. For our case, we know that there are over 1000 data entries we need

![image](https://user-images.githubusercontent.com/80243823/117675141-e6533180-b1de-11eb-9a8a-604a9a6a2826.png)

To overcome this challenge, instead of searching the whole HK Island, we acquire a list of all districts within HK Island and make multiple smaller server requests, with each request staying within the 250 limit. Then we merge the results of all requests to get a full list.
![image](https://user-images.githubusercontent.com/80243823/117676005-b5bfc780-b1df-11eb-99bc-4aac37a0b359.png)

## **Data cleansing**
After having all the data, we encounter a second problem. The data we have has to be cleansed before we could analyse it.
For example, some restaurant may have multiple tags within the same data type, like have both Japanese and Taiwanese as the cuisine; While some may have missing values and invalid data, like imcomplete addresses.
Fortunately, the proportion of such data is small, and we are able to group them and cleanse them within a day.

![image](https://user-images.githubusercontent.com/80243823/117677184-cde41680-b1e0-11eb-9f0d-df8d1c64e8ad.png)
![image](https://user-images.githubusercontent.com/80243823/117677268-e3f1d700-b1e0-11eb-91c4-54895099f6a4.png)

## **Analysis**
We first check if there is any strong correlation between the data and indeed there is. 

![image](https://user-images.githubusercontent.com/80243823/117679439-dccbc880-b1e2-11eb-9d6d-a6e7ba31ae10.png)

The more reviews a restaurant has, the more likes and bookmarks it has, which is understandable and reasonable. So we know that 'number of bookmarks' can sufficiently represent the other data. However, we don't stop here. By calculating the like/dislike ratio using the data we have, we are able to extract extra information with low correlation with existing data.
Thus, we can come up with a simple metric to estimate the profitability of a restaurant

![image](https://user-images.githubusercontent.com/80243823/117680270-94f97100-b1e3-11eb-853e-519bf3fd4252.png)
![image](https://user-images.githubusercontent.com/80243823/117680312-9fb40600-b1e3-11eb-9daf-6b959360644f.png)

## **Results**

![image](https://user-images.githubusercontent.com/80243823/117680881-2963d380-b1e4-11eb-915e-49ab979c1e19.png)
![image](https://user-images.githubusercontent.com/80243823/117681119-5b753580-b1e4-11eb-98da-a90ff3da2331.png)
![image](https://user-images.githubusercontent.com/80243823/117681222-7647aa00-b1e4-11eb-8b6c-a378486c328d.png)
![image](https://user-images.githubusercontent.com/80243823/117681273-86f82000-b1e4-11eb-914a-900bdaee4549.png)


## **Conclusion**
Without having to search for a credible database, we are able to acquire sufficient data efficiently from popular websites through Webscraping techniques. This project demonstrates that with proper Webscraping techniques and data cleansing, large amount of credible data can be acquired easily for data analysis.
