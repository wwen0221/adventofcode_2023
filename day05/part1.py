import pandas as pd


full_d = {}
seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}


results = []
temp_results = []

def read_txt(dir):
    with open(dir,'r') as f:
        data = f.read().split('\n\n')
    return data

def calc_end(x):
    x['source_end'] = int(x['source_start']) + int(x['interval'])-1
    x['destination_end'] = int(x['destination_start']) + int(x['interval'])-1
    return x

def create_df(map_name):
    current_lst = []
    current_map = full_d[map_name]
    current_map = current_map.split('\n')
    for val in current_map:
        if val != '':
            val = val.split(' ')
            val = [int(a) for a in val]
            current_lst.append(val)
 
    df = pd.DataFrame(current_lst,columns=['source_start','destination_start','interval'])
    
    #calculate the range using interval
    df = df.apply(calc_end,axis=1)

    return df

def find_source(df,value):
    new_value = value
    for idx, rows in df.iterrows():
        if value <= rows[-1] and value >= rows[1]:
            #find the difference 
            diff = rows[-1] - value
            new_value = rows[-2] - diff
    
    return new_value

if __name__ == '__main__':
    location_lst= []
    seed_to_soil_lst = []

    data = read_txt('input.txt')
    for line in data:
        (key, val) = line.split(':')
        full_d[key] = val

    seeds = full_d['seeds'].split(' ')
    seeds = [int(i) for i in seeds if i != '']

    seed_to_soil_df = create_df('seed-to-soil map')
    soil_to_fertilizer_df = create_df('soil-to-fertilizer map')
    fertilizer_to_water_df = create_df('fertilizer-to-water map')
    water_to_light_df = create_df('water-to-light map')
    light_to_temperature_df = create_df('light-to-temperature map')
    temperature_to_humidity_df = create_df('temperature-to-humidity map')
    humidity_to_location_df = create_df('humidity-to-location map')

    for seed in seeds:
        soil = find_source(seed_to_soil_df,seed)

        fert = find_source(soil_to_fertilizer_df,soil)

        water = find_source(fertilizer_to_water_df,fert)

        light = find_source(water_to_light_df,water)

        temp = find_source(light_to_temperature_df,light)

        humi = find_source(temperature_to_humidity_df,temp)

        location = find_source(humidity_to_location_df,humi)

        location_lst.append(location)

    print(min(location_lst))