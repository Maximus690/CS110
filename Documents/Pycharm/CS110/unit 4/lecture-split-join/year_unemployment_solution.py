import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    

def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
        
        
def should_keep(line, year):
    tokens = line.split()
    return tokens[1] == year

        
def get_year_metrics(lines, year):
    year_metrics = []
    for line in lines:
        if should_keep(line, year):
            year_metrics.append(line)
    return year_metrics


def find_ave_unemployment(year_metrics):
    total_ue = 0
    for line in year_metrics:
        # % Unemployment is 4th token
        record = line.split()
        unemployment = float(record[3])
        total_ue += unemployment
    return total_ue / len(year_metrics)

        
def main(input_file, year):
    lines = readlines(input_file)
    year_metrics = get_year_metrics(lines, year)
    ave_unemp = find_ave_unemployment(year_metrics)
    print(f'The average unemployment for {year} was {round(ave_unemp, 1)}')
    
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    
