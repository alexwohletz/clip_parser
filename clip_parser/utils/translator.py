import re
from tabulate import tabulate

param_pat = re.compile(r"'(?:''|[^'])*'")
param_pat_IN = re.compile(r"IN*?\s\(.*?,\n*.*?\)")
var_pat = re.compile(r"\.(\w+)")
operator_pat = re.compile(r"(<=|>=|LIKE|IN|=|>|<)")

def clean_where_clause(txt):
  '''A text string from a where clause is passed to the function and split into its component parts'''
  txt = txt.strip().replace('AND','').replace('and','').replace("%",' ')
  #Operators
  operators = re.findall(operator_pat,txt)
  #print("Operators: \n", operators)
  #print('-'*50)
  #Parameters
  params = re.findall(param_pat,txt)
  #print("Params: \n", params)
  #print('-'*50)
  #Variables
  vars = re.findall(var_pat,txt)
  #print(vars)
  #print('-'*50)

  if 'IN' in operators:
    in_ind = operators.index('IN')

    regex = r"\((.*?,\n*.*?)\)"

    param_IN = re.findall(regex,txt)
    len_IN = len(param_IN[0].split(","))
    #TODO: Make this more robust
    params[in_ind:len_IN] = [",".join(params[in_ind:len_IN])]

  table = tabulate({'Variables':vars,'Operators':operators,'Parameters':params},headers = 'keys')
  return table

if __name__ == "__main__":
  import pyperclip
  txt = \
    '''
    AND cp.from_something > '10301'
    AND cx.procedurecode IN ('12910','1010')
    AND cl.line LIKE 'approved%'
    '''
  txt = clean_where_clause(txt)
  print(txt)
  with open('test_clause.txt','w') as test:
    test.write(txt)

  