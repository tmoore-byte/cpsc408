import tests
import tables

def run():
    print("Welcome to bmw db!")
    # where I will put all functions
    user_file = str(input("Enter your desired file name: "))
    user_records = int(input("Number of records you wish to see : "))
    tables.fakeData(user_file, user_records)
    tables.fill_data(user_file)



if __name__ == '__main__':
    run()
    #tables.create_tables()

    #tests.showT()
    #tests.drop()
    #tests.showdb()


    print("completed")


