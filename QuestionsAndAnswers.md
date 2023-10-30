
## 1. How did you structure your application? Can you explain the different layers and their responsibilities? Explain your thought process.

I followed a fairly in-depth FastAPI tutorial (adapting it for the needs of this project) and used their application structure.

I decided that as a personal bonus for this project, I would learn the FastAPI framework, and treat the project as a portfolio piece. (In this way, no matter the outcome of the interview process, something of value has been produced.)

I thought about the structure as I worked.

I would probably choose to update the structure to better handle:  
* Separation of the CRUD code and the router code into separate directories. This would be preparation for handling CRUD for new types of items. Arguably it would be best to use a CRUD class that could handle a large variety of items.
* Perhaps also separate the models into their own directory as well.
* API versioning. The `api` directory would need to be renamed.

I've been looking at the large FastAPI project template stored at:
https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend


## 2. Which framework did you use to implement the API endpoints and why? What do you like about the chosen framework in particular?

I chose FastAPI.

I worked on a FastAPI project before, not directly, but on a tool that the project called. Since seeing it in action, I've wanted to study it in more detail.

It's fast, clean, and doesn't mess around. Django requires more setup.

The Swagger UI integration is also quite nice.


## 3. Did you follow any best practices in terms of code styling? How did you ensure your code is clean? What did you use in the past to ensure code quality is high and what are your experiences with such checks?

Not consciously.

I care about being able to re-read my code in the future, so that helps me write clean code in general.

I also re-read PEP8 every so often, and when I finish a milestone, I use `black` or `flake8` to check the state of the codebase. Sometimes I'll configure the style checking tool to ignore certain errors that I don't particularly mind.

In the past, I've used git hooks and/or CI tests to check code style.

My experience is that these work so long as the project has a specific person who has the authority and responsibility to manage the code style. As soon as there's a committee, code style adaptation slows down.


## 4. How did you implement persistence, what frameworks did you use and why did you choose them? Did the time constraint have an impact on your choice?

I used a second Docker container to hold a PostgreSQL database.

The DB framework was SQLAlchemy, simply because it was included in the FastAPI tutorial.

By preference, I normally use `psycopg2`.

In future, I'd like to try out `asyncpg`. From some reading, it looks like there are some speed gains.

Re: Time constraint: No.


## 5. How did you handle input validation?

Pydantic type validation. FastAPI relies on Pydantic internally and uses it to return accurate errors.


## 6. How did you handle errors and exceptions in your API? Would you handle this differently in a larger application that is going to be shipped to production?

Yes, in production you would need to limit the amount of detail in the errors, e.g. certain information should only appear in the error if the user is authenticated.


## 7. How did you ensure the uniqueness of contact identifiers? Did you use any specific technique or library?

It's an auto-incrementing numeric ID. SQLAlchemy turns autoincrement on by default on integer primary key columns.

But this does remind me: In future, I'd add a GUID field, generated with Python's `uuid` package, and use that as the publically available ID contact identifier.


## 8. How would you add authentication to the app? Explain your thought process.

Basic authentication would be an email & password. I'd send a confirmation email with a code and a link to the user (either one would confirm the ownership of the email account).

Complex authentication: Second factors for Two-Factor Authentication e.g. Google Authenticator.

Then I'd need some middleware code that could be called in the routers that handle the protected endpoints. This would check for a JWT and raise an error (or re-direct the user to the login endpoint) if the JWT is not present.


## 9. Reflect on your implementation regarding performance. What did you consider from a performance point of view? What could you improve or optimise?

I didn't consider performance.

A quick check over the endpoints shows me that:  
* The `create` method will perform an insert, which is fine.
* The `read`, `update`, and `delete` methods all use a single ID to select a contact, and this a primary key field, so there's an underlying database index, so these queries will always be quick.
* The `read_all` endpoint will become slower as more contacts are added. The solution would be to implement pagination, ensuring that future queries are reasonably speedy.


## 10. Looking back on the assignment, is there anything you would do differently? If yes, what?

Get it done on time.

Separate the router code from the CRUD code (they should be in separate directories).

Add an API versioning structure.

Write a load testing test suite using Locust.

Write integration tests that spin up test databases and confirm that the required data has been stored as expected.

Add database migrations.
