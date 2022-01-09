from datetime import datetime
import time 
from django.db.models.functions import Now
    
def test_operation(arg):
    #print("test reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    #print("test reglament: " + datetime.utcnow().isoformat())
    print("#1 test reglament: " + str(datetime.utcnow().now()))
    #print(arg)
    #print("test reglament: " + Now())
    return_result = {"status":200, "message":("test" + str(arg))}
    return return_result;

def test2_operation(arg):
    
    print("step 0 reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    
    from MetaverseDomain.com.booking import port as bookingPort
    from MetaverseFootPrint.com.booking.www.pages import reviews as bookingReviews   
    import undetected_chromedriver.v2 as uc
    
    print("step 1 reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    country = bookingPort.LanguageWeb("ua")
    
    print("step 2 reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    try:
        bookingMD = bookingPort.Phantom("uk")
    except:
        print("Error") 
    
    print("step 3 reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    hotelMD = bookingMD.getHotelByIDName(country, 'marmaros')
    
    fetchHotelReview = hotelMD.fetchReviews();
    
    if fetchHotelReview != None:
        while fetchHotelReview.next():
            print("ROW [" + str(fetchHotelReview.curentNum) + "]: ");
            print("\tb" + "UUID: " + str(fetchHotelReview.el.uuid));
            print("\tb" + "Name: " + str(fetchHotelReview.el.userName));
            print("\tb" + "Post date:"  + str(fetchHotelReview.el.post_date));
            print("\tb" + "Review bad: " + str(fetchHotelReview.el.review_bad));
            print("\tb" + "Review bad language: " + str(fetchHotelReview.el.review_bad_lang));
            print("\tb" + "Review good: " + str(fetchHotelReview.el.review_good));
            print("\tb" + "Review good language: " + str(fetchHotelReview.el.review_good_lang));
    
    
            
    '''
    #print("test reglament: " + datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z'));
    #print("test reglament: " + datetime.utcnow().isoformat())
    print("#2 test reglament: " + str(datetime.utcnow().now()))
    print(arg)
    #print("test reglament: " + Now())
    return_result = {"status":200, "message":("test" + str(arg))}
    return return_result;
    '''

def test_multioperation(arg_task, arg_operation):
    print("#4.3: Start task")

    print("#4.4: Initialization")
    return_result = {"status": 0, "message": ""}

    '''
    #Template
    if return_result["status"] == 0: 
        try:
        except Exception, e: 
            return_result["status"] = 
            return_result["message"] = "Error initialization libraty: " + str(e);
    '''
    
    if return_result["status"] == 0: 
        try:
            #from gnFantom.com.youtube.www.pages import results as findResults
            import undetected_chromedriver.v2 as uc
            import random,time,os,sys
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.by import By
            import json
        except Exception as e:
            return_result["status"] = 1
            return_result["message"] = "Error initialization libraty: " + str(e);
    
    if return_result["status"] == 0: 
        try:
            print("#4.5: Parameters")
            print(arg_operation);
            
            print("#4.6: Parameters type");
            print(type(arg_operation));
            
            if type(arg_operation).__name__ == 'str':
                arg_dict = json.loads(arg_operation)
            else:
                arg_dict = {};
                
            print('#4.7: Parameters dict')
            print(arg_dict)
                
        except Exception as e: 
            return_result["status"] = 2 
            return_result["message"] = "Error in get parameters: " + str(e);
    
    if not "url" in arg_dict:
        return_result["status"] = 3 
        return_result["message"] = "No parametr 'url'";
    
    if return_result["status"] == 0: 
        chrome_options = uc.ChromeOptions()
        
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--user_agent=DN")
        chrome_options.add_argument('--no-first-run')
        chrome_options.add_argument('--no-service-autorun')
        chrome_options.add_argument('--password-store=basic')
        
        print("#4.4: Start chrome")
        driver = uc.Chrome(options=chrome_options)
        
        #url = 'https://www.youtube.com/results?search_query=%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D0%BB%D0%BE%D0%BC%D0%BA%D0%B8';
        url = arg_dict["url"]
        driver.execute_script('window.location.href = "' + url + '"');
        
        #driver.get('https://www.youtube.com/results?search_query=%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D0%BB%D0%BE%D0%BC%D0%BA%D0%B8');
        time.sleep(5)
        
        driver.close()
        
        
    print("End task")
    
    return return_result;


            
if __name__ == '__main__':
    #test2_operation("");
    test_multioperation(2,3)