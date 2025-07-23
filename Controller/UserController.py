from flask import Blueprint, request, jsonify
from Models import RequestResponse, User
from dataclasses import asdict
from Services import UserService
import re

user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['POST'])
def createUser():
    userData = request.get_json()  
    required_fields = ["name", "email", "roleId"]
    missing_fields = [field for field in required_fields if field not in userData]

    if len(missing_fields) != 0:
        campos = missing_fields[0] if len(missing_fields) == 1 else ', '.join(missing_fields)
        return jsonify(asdict(RequestResponse(
            hasError=True,
            message=f"Campos obrigatórios {campos} faltando",
            statusCode=400
        ))), 400
    
    if (not "password" in userData):
        userData["password"] = None

    userData["name"] = userData["name"].strip()
    if not isinstance(userData.get("name"), str) or not userData["name"].strip():
        return jsonify(asdict(RequestResponse(
            hasError=True,
            message="name deve ser uma string não vazia!",
            statusCode=400
        ))), 400
    
    userData["email"] = userData["email"].strip()
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not isinstance(userData["email"], str) or not re.match(email_regex, userData["email"]):
        return jsonify(asdict(RequestResponse(
            hasError=True,
            message="email deve estar em formato válido!",
            statusCode=400
        ))), 400
    
    try:
        userData["roleId"] = int(userData["roleId"])
    except:
        return jsonify(asdict(RequestResponse(hasError=True, message=f"roleId deve ser um numero inteiro!", statusCode=400))),400
    
    try:
        userService = UserService()
        userData = User(name = userData["name"], email = userData["email"], role_id = userData["roleId"], password = userData["password"])
        user : User = userService.createUser(userData)
        return jsonify(asdict(RequestResponse(message=f"Usuario {user.id} criado!"))), 200
    except Exception as e:
        print("Erro ao criar um usuario")
        return jsonify(asdict(RequestResponse(hasError=True, message=f"Ocorreu um erro durante a solicitação, por favor tente novamente!", statusCode=500))),500


@user_bp.route('/<userId>/getRoles', methods=['GET'])
def getRolesByUserId(userId):
    try:
        userId = int(userId)
    except Exception:
        return jsonify(asdict(RequestResponse(
            hasError=True,
            message=f"userId deve ser um inteiro!",
            statusCode=400
        ))), 400

    try:
        userService = UserService()
        roles = userService.getRoles(userId)
        if(len(roles) == 0):
            return jsonify(asdict(RequestResponse(message=f"Usuario {userId} não encontrado!", data={"roles" : roles}))), 404
        return jsonify(asdict(RequestResponse(message=f"Roles do usuario {userId} encontrados!", data={"roles" : roles}))), 200
    except Exception as e:
        print(f"Erro ao obter roles do usuario {userId}")
        return jsonify(asdict(RequestResponse(hasError=True, message=f"Ocorreu um erro durante a solicitação, por favor tente novamente!", statusCode=500))),500
    
