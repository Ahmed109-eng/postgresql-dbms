from sqlalchemy import(
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)






# Creating a new sessions
Session = sessionmaker(db)
# open an actual session
session = Session()

# Creating the database using declarative subclass
base.metadata.create_all(db)


ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turin = Programmer(
    first_name = "Alan",
    last_name = "Turin",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL Language"
)
margret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)
bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)
tim_burners_lee = Programmer(
    first_name = "Tim",
    last_name = "Burners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)
ahmed = Programmer(
    first_name = "Ahmed",
    last_name = "Mahamed",
    gender = "M",
    nationality = "British",
    famous_for = "Code Institute"
)


# Add instance to session
# session.add(ada_lovelace)
# session.add(alan_turin)
# session.add(grace_hopper)
# session.add(margret_hamilton)
# session.add(bill_gates)
# session.add(tim_burners_lee)
# session.add(ahmed)

# Commit the session
session.commit()


programmers = session.query(Programmer)

# programmer = session.query(Programmer).filter_by(id=2).first()
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")

# programmer = session.query(Programmer).filter_by(first_name = fname, last_name = lname).first()
# if programmer is not None:
#     print("Programmer found:", programmer.first_name, programmer.last_name)
#     confirm = input("Do you want to delete this record? (y/n)")
#     if confirm.lower() == "y":
#         session.delete(programmer)
#     else:
#         print("Programmer not deleted")

# else:
#     print("Programmer not found: ")


for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )