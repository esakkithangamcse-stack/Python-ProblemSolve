def poster_page_sort(pages):
    sort_pages = sorted(pages)
    new_page_order = []
    
    if len(pages)/2 == 0:
        unpair = False
    else:
        unpair= True
    for index, n in enumerate(sort_pages):
        if index<len(pages)//2:
            new_page_order.append(sort_pages[-(index+1)])
            new_page_order.append(sort_pages[index])
        else:
            if unpair:
                new_page_order.append(sort_pages[index])
            break
        
    return new_page_order
           
if __name__ == "__main__":
    print(poster_page_sort([4,2,7,3,1,24,6]))