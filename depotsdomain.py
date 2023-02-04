from Action import Action


def get_actions():
    actions = []
    locations = ['1','2','3']
    boxes = ['A','B','C']
    plates = ['4','5','6']
    for loc in locations:
        for loc1 in locations:
            if(loc==loc1):
                continue
            else:
                emptyDrive=  Action(name ='drive from' + loc + ' to '+loc1,positive_preconditions=['TruckAt'+loc],\
                        negative_preconditions=[],add_list=["TruckAt"+loc1],delete_list=["TruckAt"+loc])
                actions.append(emptyDrive)
                for b in boxes:
                    drive= Action(name ='drive from' + loc + ' to '+loc1,positive_preconditions=['TruckAt'+loc,b+'onTruck'],\
                        negative_preconditions=[],add_list=["TruckAt"+loc1,"Box"+b+'At'+loc1],delete_list=["TruckAt"+loc])
                    actions.append(drive)

        for b in boxes:
            for bx in boxes:
                if(b==bx):
                    continue
                else:
                    for p in plates:
                        lift=Action(name='lift '+b+' to '+p,positive_preconditions=["TruckAt"+loc,"Box"+b+"At"+loc,\
                            "Box"+bx+"At"+loc,bx+"plate"+p,"clear"+bx,b+"onfloor"],negative_preconditions=[],add_list=[b+"on"+bx,b+"plate"+p],delete_list=["clear"+bx,b+"onfloor"])
                        actions.append(lift)
                        drop=Action(name='drop '+b+' from '+p,positive_preconditions=["TruckAt"+loc,"Box"+b+"At"+loc,\
                                b+"plate"+p,"clear"+b],negative_preconditions=[],add_list=[b+"onfloor"],delete_list=[b+"plate"+p])
                        actions.append(drop)
                
            load=Action(name='load box'+b+' from '+loc,positive_preconditions=["TruckAt"+loc,"Box"+b+"At"+loc,b+"onfloor"],\
                negative_preconditions=[],add_list=[b+"onTruck"],delete_list=[b+"onfloor"])
            unload=Action(name='unload box'+b+' in '+loc,positive_preconditions=["TruckAt"+loc,"Box"+b+"At"+loc,\
                b+"onTruck"],negative_preconditions=[],add_list=[b+"onfloor"],delete_list=[b+"onTruck"])
            actions.append(load)
            actions.append(unload)
            
    return actions