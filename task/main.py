import login
import projects

def main():
    while True:
        print("\n Welcome to the Crowd-Funding App")
        print("1️⃣ Register")
        print("2️⃣ Login")
        print("3️⃣ Search by date ..")
        print("4️⃣ Exit")

        ch=input("Enter your choice ")
        print("************************************")
        match ch:
            case "1":
                login.register()
            case "2":
                user=login.login()
                
                if user :
                    print("✅ Successfully logged in")
                    user_email = user["email"]
                    user_name = user["f_name"]
                    user_name2 = user["l_name"]
                    while True :
                            print("\n Welcome " , user_name , user_name2)
                            print("1️⃣ View all projects ")
                            print("2️⃣ View my projects ")
                            print("3️⃣ Create project")
                            print("4️⃣ Delete project")
                            print("5️⃣ Edit project")
                            print("6️⃣ Logout")

                            ch2=input("Enter your choice ")
                            print("************************************")
                            match ch2:
                                case "1":
                                    projects.view_projects()
                                case "2":
                                    projects.view_my_projects(user_email)
                                case "3":
                                    projects.create_project(user_email)

                                case "4":
                                    projects.delete_project(user_email)

                                case "5":
                                    projects.edit_project(user_email)
                                case "6":
                                    login.logout(user_email)
                                    break
                                case _ :
                                    print("invalid choice ")

            
            case "4":
                print("bye")
                break
            case "3" :
                projects.search_by_date()
            case _:
                print("invalid choice")
if __name__== "__main__":
    main()
            
