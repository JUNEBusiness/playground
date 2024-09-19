from flask import Flask, abort, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("title", required=False, type=str)
parser.add_argument("book", required=False, type=str)

# Initialize a dictionary of books
# bookstore_inventory = {
#     "book1": {
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald",
#         "genre": "Fiction",
#         "price": 10.99,
#         "quantity_in_stock": 3,
#         "isbn": "978-3-16-148410-0"
#     },
#     "book2": {
#         "title": "To Kill a Mockingbird",
#         "author": "Harper Lee",
#         "genre": "Fiction",
#         "price": 7.99,
#         "quantity_in_stock": 5,
#         "isbn": "978-0-7432-7356-5"
#     },
#     "book3": {
#         "title": "1984",
#         "author": "George Orwell",
#         "genre": "Dystopian",
#         "price": 8.99,
#         "quantity_in_stock": 2,
#         "isbn": "978-0-452-28423-4"
#     },
#     "book4": {
#         "title": "The Catcher in the Rye",
#         "author": "J.D. Salinger",
#         "genre": "Fiction",
#         "price": 6.99,
#         "quantity_in_stock": 4,
#         "isbn": "978-0-670-82162-4"
#     },
#     "book5": {
#         "title": "Brave New World",
#         "author": "Aldous Huxley",
#         "genre": "Dystopian",
#         "price": 9.99,
#         "quantity_in_stock": 6,
#         "isbn": "978-0-06-112008-4"
#     },
#     "book6": {
#         "title": "The Road",
#         "author": "Cormac McCarthy",
#         "genre": "Post-Apocalyptic",
#         "price": 12.99,
#         "quantity_in_stock": 1,
#         "isbn": "978-0-307-27778-1"
#     },
#     "book7": {
#         "title": "The God of Small Things",
#         "author": "Arundhati Roy",
#         "genre": "Fiction",
#         "price": 14.99,
#         "quantity_in_stock": 2,
#         "isbn": "978-0-14-028329-7"
#     }
# }

with open("bookstore_inventory.json", "r") as f:
    bookstore_inventory = json.load(f)

def write_changes_to_file():
    global bookstore_inventory
    with open("bookstore_inventory.json", "w") as f:
        json.dump(bookstore_inventory, f)



class BookStore(Resource):

    def get(self, book_id="all"):
        if book_id == "all":
            return bookstore_inventory
        return bookstore_inventory[book_id]
    


class Book(Resource):
    
    def put(self):
        data= request.form
        book_id=data.get("book_id")
        if book_id in bookstore_inventory:
            bookstore_inventory[book_id] = {
                                                "title": data.get("title"),
                                                "author": data.get("author"),
                                                "genre": data.get("genre"),
                                                "price": data.get("price"),
                                                "quantity_in_stock": data.get("quantity_in_stock"),
                                                "isbn": data.get("isbn")
                                            }
            write_changes_to_file()
            return {"message": f"{book_id} updated successfully", "status code":201}, 201
        abort(404, message=f"{book_id} not found")


    def delete(self, book_id):
        if book_id in bookstore_inventory:  
            del bookstore_inventory[book_id]
            write_changes_to_file()
            return {"message": f"{book_id} deleted successfully", "status code":204}
        abort(404, message=f"{book_id} not found")

    def post(self):
        data= request.get_json()
        title = data["title"]
        book_id = "book" + str(max(int(v.lstrip("book")) for v in bookstore_inventory.keys()) + 1)
        print(data, title)
        if book_id not in bookstore_inventory:
            for key in bookstore_inventory.values():
                print(key)
                if key["title"] == title:
                    return {"message":f"Book title:{title} already exists."}
            bookstore_inventory[book_id] = {
                                                "title": title,
                                                "author": data.get("author"),
                                                "genre": data.get("genre"),
                                                "price": data.get("price"),
                                                "quantity_in_stock": data.get("quantity_in_stock"),
                                                "isbn": data.get("isbn")
                                            }
            write_changes_to_file()
            return {"message": f"{book_id} updated successfully", "status code":201}, 201
        abort(404, message=f"{book_id} already exists.")

    

api.add_resource(BookStore, "/books/<string:book_id>", "/")
api.add_resource(Book, "/books/update/", "/books/delete/<string:book_id>", "/books/create/")

if __name__=="__main__":
    app.run(debug=True)
    
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))