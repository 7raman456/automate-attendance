import requests
d={
    "entry.1628776034":"2 ADITYA DEV PRASAD"
    
}

l=requests.get("https://docs.google.com/forms/d/e/1FAIpQLSdB3PXiYu7VcN3L6A31j_By1XtIGEVAzeBkWzNsAFnjMAgE7A/formResponse",d)
