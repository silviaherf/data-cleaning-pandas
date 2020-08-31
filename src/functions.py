##Funciones utilizadas en el archivo de código jupyter notebook

##Esta función finalmente no se utiliza

def depure_activity(x):
    if type(x)==str:
        if x.replace(r"(.*)urfing(.*)",'Surfing')==True:
            x=x.replace(r"(.*)urfing(.*)",'Surfing')
            return x
        if x.replace(r"(.*)wimming(.*)",'Swimming')==True:
            x=x.replace(r"(.*)wimming(.*)",'Swimming')
            return x
        if x.replace(r"(.*)ishing(.*)",'Fishing')==True:
            x=x.replace(r"(.*)ishing(.*)",'Fishing')
            return x
        if x.replace(r"(.*)pearfishing(.*)",'Spearfishing')==True:
            x=x.replace(r"(.*)pearfishing(.*)",'Spearfishing')
            return x
        if x.replace(r"(.*)athing(.*)",'Bathing')==True:
            x=x.replace(r"(.*)bathing(.*)",'Bathing')
            return x
        if x.replace(r"(.*)Wading(.*)",'Wading')==True:
            x=x.replace(r"(.*)Wading(.*)",'Wading')
            return x
        if x.replace(r"(.*)Diving(.*)",'diving')==True:
            x=x.replace(r"(.*)Diving(.*)",'diving')
            return x
        if x.replace(r"(.*)tanding(.*)",'Standing')==True:
            x=x.replace(r"(.*)tanding(.*)",'Standing')
            return x
        if x.replace(r"(.*)norkeling(.*)",'Snorkeling')==True:
            x=x.replace(r"(.*)norkeling(.*)",'Snorkeling')
            return x
        if x.replace(r"(.*)Scuba diving(.*)",'Scuba diving')==True:
            x=x.replace(r"(.*)Scuba diving(.*)",'Scuba diving')
            return x

