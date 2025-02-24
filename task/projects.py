import json 
import os 
from datetime import datetime

PROJECT_FIle="projects.json"
# print("❌ Please enter a valid date.")

def load_projects():
    if os.path.exists(PROJECT_FIle):
        with open(PROJECT_FIle ,"r") as file:
            content = file.read().strip()
            if not content :
                return []
            return json.loads(content)
    return []

def save_projects(projects):
    with open(PROJECT_FIle,"w") as file:
        return json.dump(projects,file,indent=4)


def validate_dates(start_date , end_date ):
    try:

        start = datetime.strptime(start_date,"%Y-%m-%d")
        end = datetime.strptime(end_date,"%Y-%m-%d")
        return start<end
    except ValueError:
        return False




def create_project(user_email):
    projects=load_projects()
    title=input("Enter project name : ")
    details=input("Enter project details : ")

    total_target = input("Enter project amount: ")

    try:
        total_target = float(total_target)  
        print("Valid number:", total_target)
    except ValueError:
        print("Invalid number ❌") 
        return
    
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    if not validate_dates(start_date,end_date):
        print ("not valid date make sure start and ednd dates ❌")
        return
    project = {
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_date": start_date,
        "end_date": end_date,
        "owner": user_email
    }

    projects.append(project)
    save_projects(projects)
    print("Project created successfully!")


def view_projects():
    projects = load_projects()
    if not projects:
        print ("no projects yet ❌")
        return

    for index , project in enumerate(projects,1):
        print("************************************")
        print("All Projects ")
        print("************************************")

        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Total Target: {project['total_target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
        print(f"Owner: {project['owner']}")
        print("************************************")


def view_my_projects(user_email):
    projects = load_projects()

    user_project= [p for p in projects if p["owner"]==user_email]

    if not user_project:
        print ("no projects yet ❌")
        return

    for index , project in enumerate(user_project,1):
        print("************************************")
        print("Your Projects are ")
        print("************************************")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Total Target: {project['total_target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
        print(f"Owner: {project['owner']}")
        print("************************************")




def delete_project(user_email):
    projects =load_projects()
    user_projects = [p for p in projects if p["owner"] == user_email]

    if not user_projects :
        print ("you havn't any projects ❌ ")
        return 
    
    view_projects()
    proj_title = input ("Please Enter name of project you want delete ")

    for project in projects :
        if proj_title==project["title"].strip().lower() and project["owner"] == user_email :
            projects.remove(project)
            save_projects(projects)
            print("Project deleted successfully!")
            return
    print("Project not found or you don't have permission to delete it.")



def edit_project(user_email):
    projects = load_projects()

    user_projects = [p for p in projects if p["owner"] == user_email]

    if not user_projects:
        print("You haven't any projects ❌")
        return

    view_projects()

    proj_title = input("Please enter the name of the project you want to edit: ").strip().lower()

    for project in projects:
        if proj_title == project["title"].strip().lower() and project["owner"] == user_email:
            project['title'] = input("Enter new title (leave blank to keep current): ") or project['title']
            project['details'] = input("Enter new details (leave blank to keep current): ") or project['details']

            try:
                new_target = input("Enter new total target (leave blank to keep current): ")
                project['total_target'] = float(new_target) if new_target else project['total_target']
            except ValueError:
                print("Invalid amount. Keeping the old value.")

            start_date = input("Enter new start date (YYYY-MM-DD, leave blank to keep current): ") or project['start_date']
            end_date = input("Enter new end date (YYYY-MM-DD, leave blank to keep current): ") or project['end_date']

            if not validate_dates(start_date, end_date):
                print("Invalid date range. Keeping the old values.")
            else:
                project['start_date'] = start_date
                project['end_date'] = end_date

            save_projects(projects)  
            print("Project updated successfully!")
            return  

    print("Project not found or you don't have permission to edit it.")  



def search_by_date():
    projects=load_projects()

    proj_date=input("Enter project date you want find .. : ").strip()

    if not proj_date:
        print("Wrong enter any date .. ❌")
        return

    result = [p for p in projects if p["start_date"] <= proj_date <= p["end_date"]]
     
    if result:
        print(" Found Projects:")
        for project in result:
            print(f"\nTitle: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total Target: {project['total_target']} EGP")
            print(f"Start Date: {project['start_date']}")
            print(f"End Date: {project['end_date']}")
            print(f"Owner: {project['owner']}")
    else:
        print(" No projects found with this name ❌")



    


    
    


    



