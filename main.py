def main():
    person = {"name": "foo", "age": 30}
    
    person.update({ "age": 31})
    print(person)
    
    person.update({ "name": "bar" });
    person.update({ "name": "bar" });
    person.update({ "name": "baz" });
    person.update({ "name": "baz" });
    person.update({ "age": 31 });
    person.update({ "age": 32 });


if __name__ == "__main__":
    main()
