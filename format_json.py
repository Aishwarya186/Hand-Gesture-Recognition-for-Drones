import os, json, re



# As input I would get a directory. In which are jsonfiles.
# Out put a json file containing all the json files.



def json_join(json_dir, labels):
    big_json = {'data':{},'label':'hey'}
    

    vid_id = re.findall(r'/([0-9]+)$',json_dir)[0]


    for file_name in os.listdir(json_dir):
        with open(os.path.join(json_dir,file_name), 'r', encoding='utf-8-sig') as f:
            json_file = json.load(f)
            
        #print("before frame \n")
        frame = re.findall(r'([0-9]|[1-9][0-9]|1[0-9][0-9])', file_name )[0]
        #print("\n frames", frame)
        big_json['data'][frame] = json_file['people']
  
    # Look up the label somewhere
    big_json['label'] = labels[vid_id]
    big_json['id'] = vid_id


    return big_json

