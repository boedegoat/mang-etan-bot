from replit import db
import msg

write = msg.Formatting()

# default respond
if 'respond' not in db.keys() :
  db['respond'] = False

def get_data_respond() :
  return db['respond']

def set_data_respond(bool) :
  if 'respond' in db.keys() :
    db['respond'] = bool

def store_data(data) :
  # jika key 'datalist' udh ada
  if 'datalist' in db.keys() :
    # get valuenya lalu masukin ke variable
    datalist = db['datalist']

    # tambahkan data
    datalist.append(data)

    # masukin lagi ke key 'datalist'
    db['datalist'] = datalist

  else :
    db['datalist'] = [data]

def get_data() :
  return db['datalist']

def delete_data(index) :
  datalist = db['datalist']
  if len(datalist) > index :
    deleted = datalist[index]
    del datalist[index]
    db['datalist'] = datalist
    return(f'''
    {write.bold(deleted)} berhasil di hapus
    sisa : {get_data()}
    ''')
  else :
    return 'Error : Index melebihi jumlah data'