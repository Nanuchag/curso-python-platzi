import utils

data = [
  {
    'Country' : 'Argentina',
    'Population': 6000
   },
  {
    'Country': 'Brasil',
    'Population': 4000
  },
  {
    'Country': 'Colombia',
    'Population': 5500
  },
  {
    'Country': 'Uruguay',
    'Population': 3500
  },
  {
    'Country': 'Chile',
    'Population': 3200
  }
  
]
def run():
  keys, values = utils.get_population()
  print(keys, values)
  
  #print(utils.A)
  country = input('Type country => ')
  
  result = utils.population_by_country(data, country)
  print(result)

if __name__ == '__main__':
  run()