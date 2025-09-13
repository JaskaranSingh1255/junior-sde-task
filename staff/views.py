from rest_framework.decorators import api_view
from rest_framework.response import Response
from bson import ObjectId
from .mongo import collection
from datetime import datetime

def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@api_view(['POST'])
def create_employee(request):
    data = request.data
    if collection.find_one({"employee_id": data.get("employee_id")}):
        return Response({"error": "Employee ID must be unique"}, status=400)
    collection.insert_one(data)
    return Response({"message": "Employee created"}, status=201)

@api_view(['GET'])
def get_employee(request, employee_id):
    emp = collection.find_one({"employee_id": employee_id})
    if not emp:
        return Response({"error": "Not found"}, status=404)
    return Response(serialize(emp))

@api_view(['PUT'])
def update_employee(request, employee_id):
    data = request.data
    result = collection.update_one({"employee_id": employee_id}, {"$set": data})
    if result.matched_count == 0:
        return Response({"error": "Not found"}, status=404)
    return Response({"message": "Updated"})

@api_view(['DELETE'])
def delete_employee(request, employee_id):
    result = collection.delete_one({"employee_id": employee_id})
    if result.deleted_count == 0:
        return Response({"error": "Not found"}, status=404)
    return Response({"message": "Deleted"})

@api_view(['GET'])
def list_by_department(request):
    dept = request.GET.get("department")
    emps = collection.find({"department": dept}).sort("joining_date", -1)
    return Response([serialize(e) for e in emps])

@api_view(['GET'])
def avg_salary(request):
    pipeline = [
        {"$group": {"_id": "$department", "avg_salary": {"$avg": "$salary"}}},
        {"$project": {"department": "$_id", "avg_salary": 1, "_id": 0}}
    ]
    result = list(collection.aggregate(pipeline))
    return Response(result)

@api_view(['GET'])
def search_by_skill(request):
    skill = request.GET.get("skill")
    emps = collection.find({"skills": skill})
    return Response([serialize(e) for e in emps])

@api_view(['GET'])
def paginated_employees(request):
    page = int(request.GET.get("page", 1))
    size = int(request.GET.get("size", 5))
    skip = (page - 1) * size
    emps = collection.find().skip(skip).limit(size)
    return Response([serialize(e) for e in emps])
