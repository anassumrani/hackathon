from application import db
from sqlalchemy import delete
from application.models import Customers, Packages, Drivers
from datetime import datetime

db.create_all()

Customer1 = Customers(customer_name = "Harry Johnson", customer_address = "5 Northload St, Glastonbury,Somerset, BA6 9JJ", customer_email = "harryj..n@gmail.com", customer_phone_number = "01458 831882")
Customer2 = Customers(customer_name = "Ben Woodford", customer_address = "Charlotte Pl, Southampton SO14 0TB, United Kingdom", customer_email = "ben10wood@hotmail.com", customer_phone_number = "07858 831882")
Customer3 = Customers(customer_name = "Adam Gray", customer_address = "17 St John St, Manchester M3 4DR, United Kingdom", customer_email = "adam123456789@gmail.com", customer_phone_number = "07098 831882")
Customer4 = Customers(customer_name = "Leon Weeks", customer_address = "27 Sale Pl, Tyburnia, London W2 1YR, United Kingdom", customer_email = "leon-king@yahoo.com", customer_phone_number = "076415869147")
Customer5 = Customers(customer_name = "Harry Hetherington", customer_address = "124 Oxford Rd, Reading RG1 7NL, United Kingdom", customer_email = "hairyharry@outlook.com", customer_phone_number = "07364158951")
Customer6 = Customers(customer_name = "Subit Gurung", customer_address = "23 Queen Square, London WC1N 3BG, United Kingdom", customer_email = "sobersubit@gmail.com", customer_phone_number = "07698547521")
Customer7 = Customers(customer_name = "Samuel Marten", customer_address = "100 Harley St, Marylebone, London W1G 7JA, United Kingdom", customer_email = "sam788@gmail.com", customer_phone_number = "07631125981")
Customer8 = Customers(customer_name = "Tasnim Begum", customer_address = "Spire London East Hospital, Roding Ln S, London IG4 5PZ, United Kingdom", customer_email = "tasnimb@gmail.com", customer_phone_number = "07369854751")
Customer9 = Customers(customer_name = "konrad Kantorski", customer_address = "38 Baileyfield Rd, Edinburgh EH15 1NA, United Kingdom", customer_email = "killer-konrad@yahoo.com", customer_phone_number = "06321479554")
Customer10 = Customers(customer_name = "Prakash Thapa", customer_address = "39 Mile End Rd, Bethnal Green, London E1 4TP, United Kingdom", customer_email = "PR4K45TH4P4@GMAIL.COM", customer_phone_number = "079865553666")


