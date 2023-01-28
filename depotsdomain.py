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
                drive= Action(name ='drive from' + loc + ' to '+loc1,positive_preconditions=['Truck at '+loc],\
                    negative_preconditions=["Not equal"+loc+' '+loc1],add_list=["Truck at"+loc1],delete_list=["Truck at"+loc])
                actions.append(drive)

        for b in boxes:
            for bx in boxes:
                if(b==bx):
                    continue
                else:
                    for p in plates:
                        lift=Action(name='lift '+b+' to '+p,positive_preconditions=["Truck at"+loc,"Box "+b+"at "+loc,\
                            bx+" at "+loc,bx+" in plate "+p,"clear on"+bx],negative_preconditions=[],add_list=[b+" on "+bx,b+" in plate "+p],delete_list=[])
                        actions.append(lift)

            drop=Action(name='drop '+b+' from '+p,positive_preconditions=["Truck at"+loc,"Box "+b+"at "+loc,\
                b+" in plate "+p,"clear on"+b],negative_preconditions=[],add_list=[],delete_list=[b+" in plate "+p])
                        
            load=Action(name='load box'+b+' from '+loc,positive_preconditions=["Truck at"+loc,"Box "+b+"at "+loc, "clear on "+b,b+" on floor"],\
                negative_preconditions=[],add_list=[b+" on Truck"],delete_list=[b+" on floor"])
            unload=Action(name='unload box'+b+' in '+loc,positive_preconditions=["Truck at"+loc,"Box "+b+"at "+loc,\
                b+" on Truck"],negative_preconditions=[],add_list=[b+" on floor"],delete_list=[b+" on Truck"])
            actions.append(load)
            actions.append(unload)
            actions.append(drop)
    return actions