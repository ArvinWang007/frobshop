
#If two models with the same name are declared within an app, 
#Django will only use the first one. 
#That means that if you wish to customise Oscar’s models,
#you must declare your custom ones before 
#importing Oscar’s models for that app.


#your custom models go here



from oscar.app.order.models import *
