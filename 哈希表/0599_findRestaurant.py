class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {restaurant: i for i, restaurant in enumerate(list1)}
        best_restaurants = []
        min_index_sum = float('inf')
        for idx2, restaurant in enumerate(list2):

            if restaurant in index_map:
                index_sum = idx2 + index_map[restaurant]

                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    best_restaurants = [restaurant]
                    
                elif index_sum == min_index_sum:
                    best_restaurants.append(restaurant)
        
        return best_restaurants