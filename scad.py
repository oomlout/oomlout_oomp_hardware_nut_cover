import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    #oomp_mode = "project"
    oomp_mode = "oobb"

    test = False
    #test = True

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
        #default
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #default
        #filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
        part_default["project_name"] = "oomlout_oomp_hardware_nut_cover" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        

        sizes = []
        sizes.append([20,20,9])
        sizes.append([14,14,9])
        sizes.append([10,10,9])

        names = ["nut_cover_slide", "nut_cover_push"]



        extra = "m6"
        for size in sizes:
            for name in names:                
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = size[0]
                p3["height"] = size[1]
                p3["thickness"] = size[2]
                p3["extra"] = extra
                part["kwargs"] = p3
                part["name"] = name
                parts.append(part)

        extra = "m3"
        sizes = []        
        sizes.append([10,10,6])
        sizes.append([6,6,6])
        for size in sizes:
            for name in names:                
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = size[0]
                p3["height"] = size[1]
                p3["thickness"] = size[2]
                p3["extra"] = extra
                part["kwargs"] = p3
                part["name"] = name
                parts.append(part)


    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    
    width_label = kwargs.get("width_label", 1)
    height_label = kwargs.get("height_label", 1)

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "left"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #label holder big piece
    if True:
        extra_label_border = 4
        extra_label_clearance = 2
        depth_label_inset = 1   
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"rounded_rectangle"
        wid = width_label + extra_label_border
        hei = height_label + extra_label_border
        dep = depth
        size = [wid, hei, dep]
        p3["size"] = size
        p3["radius"] = 3 + extra_label_border/2
        p3["depth"] = dep
        p3["both_holes"] = True
        p3["holes"] = "left"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += hei/2
        pos1[2] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #inset

        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        wid = width_label + extra_label_clearance
        hei = height_label + extra_label_clearance
        dep = depth_label_inset
        size = [wid, hei, dep]
        p4["size"] = size
        p4["radius"] = 3 + extra_label_clearance/2
        
        p4["both_holes"] = True
        p4["holes"] = "left"
        p4["m"] = "#"
        pos11 = copy.deepcopy(pos1)
        pos11[2] += 0#depth - depth_label_inset - dep/2
        p4["pos"] = pos11        
        oobb_base.append_full(thing,**p4)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_nut_cover_push(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "m6")

    radius_name = extra
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    diameter = 20
    depth_lip = 1.5

    #add cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"    
    w = width
    h = height
    d = depth
    size = [w,h,d]
    p3["size"] = size
    #p3["depth"] = depth
    #p3["radius"] = diameter/2
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add nut
    
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_nut"
    p3["radius_name"] = radius_name
    p3["clearance"] = "side"
    p3["extra_clearance"] = -0.25
    pos1 = copy.deepcopy(pos)
    #pos1[2] += depth_lip
    p3["pos"] = pos1
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add m6 hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = radius_name
    p3["clearance"] = "side"
    p3["depth"] = depth
    #p3["width"] = 10
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += -depth/2 + depth_lip
    pos1[0] += 5
    p3["pos"] = pos1
    #oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_nut_cover_slide(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "m6")

    radius_name = extra
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    diameter = 20
    depth_lip = 1.5

    #add cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"    
    w = width
    h = height
    d = depth
    size = [w,h,d]
    p3["size"] = size
    #p3["depth"] = depth
    #p3["radius"] = diameter/2
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add nut
    
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_nut"
    p3["radius_name"] = radius_name
    p3["clearance"] = "side"
    p3["extra_clearance"] = 1
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth_lip
    poss = []
    pos11 = copy.deepcopy(pos1)
    poss.append(pos11)
    copies = 3
    shift_x = 5   
    for i in range(copies):
        pos11 = copy.deepcopy(pos1)            
        pos11[0] += i+1*shift_x        
        poss.append(pos11)
    
    p3["pos"] = poss
    p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    #add m6 slot
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_slot"
    p3["radius_name"] = radius_name
    p3["clearance"] = "side"
    p3["depth"] = depth
    p3["width"] = 10
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += -depth/2 + depth_lip
    pos1[0] += 5
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)