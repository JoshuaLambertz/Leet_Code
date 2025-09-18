"""
Design a food rating system that can do the following:
    Modify the rating of a food item listed in the system.
    Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:
    FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system.
    The food items are described by foods, cuisines and ratings, all of which have a length of n.

    foods[i] is the name of the ith food,
    cuisines[i] is the type of cuisine of the ith food, and
    ratings[i] is the initial rating of the ith food.

    void changeRating(String food, int newRating) Changes the rating of the food item with the name food.

    String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine.
    If there is a tie, return the item with the lexicographically smaller name.

Example:
    Input:
        ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
        [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
    Output:
        [null, "kimchi", "ramen", null, "sushi", null, "ramen"]
"""

import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.foodToCuisine = dict(zip(foods, cuisines))
        self.foodToRating = dict(zip(foods, ratings))

        self.cuisineHeaps = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.cuisineHeaps:
                self.cuisineHeaps[cuisine] = []

            heapq.heappush(self.cuisineHeaps[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        self.foodToRating[food] = newRating

        cuisine = self.foodToCuisine[food]
        heapq.heappush(self.cuisineHeaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisineHeaps[cuisine]

        while heap:
            rating, food = heap[0]
            rating = -rating
            if self.foodToRating[food] == rating:
                return food
            else:
                #Lazy deletion
                heapq.heappop(heap)