class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection:list, items_per_page:int):
        self._page_list=[]
        self._items_per_page=items_per_page
        self._total_items=len(collection)
        for i in range(0, self._total_items, self._items_per_page):
            self._page_list.append(collection[i:i + self._items_per_page])
    
    # returns the number of items within the entire collection
    def item_count(self)->int:
        return self._total_items
    
    # returns the number of pages
    def page_count(self)->int:
        return len(self._page_list)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index:int)->int:
        if(page_index<0 or page_index>=self.page_count()):
            return -1
        return len(self._page_list[page_index])
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index:int)->int:
        if(item_index>=self.item_count() or item_index<0):
            return -1
        page,_=divmod(item_index,self._items_per_page)
        return page



collection = ['a','b','c','d','e','f']
helper = PaginationHelper(collection, 4)
print(helper.page_count() == 2, 'page_count is returning incorrect value.')
print(helper.item_count() == 6, 'item_count returned incorrect value')
print(helper.page_item_count(0) == 4, 'page_item_count returned incorrect value for page_index 0')
print(helper.page_item_count(1) == 2, 'page_item_count returned incorrect value for page_index 1')
print(helper.page_item_count(2) ==-1, 'page_item_count returned incorrect value for page_index 2')