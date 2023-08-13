def read_file(path):
    with open(path, 'r') as f:
        uff_data = f.read()
        f.close()

    # print(uff_data)

    # Split the string into a list
    lines = uff_data.split("026")
    # Remove both of the first and last lines
    lines = lines[1:-1]
    # Store the split data
    result = []
    for line in lines:
        # Initialize the data structure
        init_data = {
            "an_mpan": "",
            "state": "",
            "meter_serial_number": "",
            "reading_type": "",
            "meter_register_id": "",
            "reading_date_time": "",
            "register_reading": "",
            "meter_reading_flag": "",
            "reading_method": "",
        }

        data = line.split("\n")
        # Iterate through the data and process it
        for i in range(len(data) - 1):
            if i == 0:
                an_mpan_data = data[i].split("|")
                # data from 026
                init_data["an_mpan"] = an_mpan_data[1]
                init_data["state"] = an_mpan_data[2]
            elif i == 1:
                meter_serial_number_data = data[i].split("|")
                # data from 028
                init_data["meter_serial_number"] = meter_serial_number_data[1]
                init_data["reading_type"] = meter_serial_number_data[2]
            else:
                meter_register_data = data[i].split("|")
                # data from 030
                init_data["meter_register_id"] = meter_register_data[1]
                init_data["reading_date_time"] = meter_register_data[2]
                init_data["register_reading"] = meter_register_data[3]
                init_data["meter_reading_flag"] = meter_register_data[6]
                init_data["reading_method"] = meter_register_data[7]
                result.append(init_data)

    print(str(result).replace("\'", "\""))
    return result


if __name__ == '__main__':
    uff_file_path = '../test.uff'
    read_file(uff_file_path)
