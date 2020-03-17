from bs4 import BeautifulSoup
import requests

def findInList(listToSearch, item):
    try:
        retval=listToSearch.index(item)
        #print(retval)
        return retval
    except:
        return -1

def getQuestionsAndOptions(questionsList):

    #nextQuestionStarted=False
    #hasReferenceChanged=False

    questionObject=[]
    questionDict={}
    options=0
    questionRef=""

    for question in questionsList:
        classList=question.get("class")
        #print(classList)
        if(findInList(classList,"quslist")>-1):        
            #nextQuestionStarted=True        
            questionObject.append(questionDict)
            questionDict={}
            
            questionReference=question.find("div",{"class": "qus_ref"})
            
            if(questionReference):
                #hasReferenceChanged=True
                questionRef=questionReference.text
            
            questionDict["questionReference"]=questionRef
            questionDict["question"]=question.text
            option=0
            
        

        if(findInList(classList,"optdiv")>-1):        
        
            questionDict["option_"+str(option)]=question.text
            option=option+1
            
        if(findInList(classList,"exp_text")>-1):   
            questionDict["explaination"]=question.text
            img=question.find("img")
            if(img):
                questionDict["image_explaination"]=img.get("src")

            
        if(findInList(classList,"crct")>-1):    
            questionDict["correct_answer"]=question.find("span").text


    questionObject.append(questionDict)
    
    return questionObject


    

URL_List=["https://www.fresherslive.com/online-test/alphabet-sequence-questions-and-answers/", "https://www.fresherslive.com/online-test/direction-sense-questions-and-answers",'https://www.fresherslive.com/online-test/symbols-questions-and-answers', 'https://www.fresherslive.com/online-test/series-questions-and-answers']    
pagesCount=[20,1,6,12]

for i in range(0, len(URL_List)):
    URL=URL_List[i]
    pages=pagesCount[i]
    for pagenumber in range (1,pages+1) :
        indexURL=URL+str(pagenumber)    
        html_doc=requests.get(indexURL)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        questionList=soup.find("div", {"class": "quswrap"}).find_all("div")
        extractedData=getQuestionsAndOptions(questionList)
        print(extractedData)
    #exit()



