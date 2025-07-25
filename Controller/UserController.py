from flask import Blueprint, request, jsonify
from Models import User
from Schemas import RequestResponse
from dataclasses import asdict
from Services import UserService
import re
from Utils import getLogger
import traceback

user_bp = Blueprint('user', __name__)
logger = getLogger(__name__)

@user_bp.route('/', methods=['POST'])
def createUser():
    logger.info("Requisição para criar usuario recebida")
    try:
        userData = request.get_json()  
    except Exception as e:
        stacktrace = traceback.format_exc() 
        logger.error(f"Erro ao tentar converter JSON do body. Erro: {str(e)}. Stacktrace: {stacktrace}")
        return jsonify(asdict(RequestResponse(hasError=True, message=f"JSON fornecido no body é invalido!", statusCode=404))),404

    requiredFields = ["name", "email", "roleId"]
    logger.info(f"Validando existencia dos campos {', '.join(requiredFields)}")
    missingFields = [field for field in requiredFields if field not in userData]

    if len(missingFields) != 0:
        campos = missingFields[0] if len(missingFields) == 1 else ', '.join(missingFields)
        logger.warning(f"Requisição com os campos {campos} faltando")
        return jsonify(asdict(RequestResponse(
            hasError=True,
            message=f"Campos obrigatórios {campos} faltando",
            statusCode=400
        ))), 400
    
    if (not "password" in userData):
        userData["password"] = None

    userData["name"] = userData["name"].strip()
    if not isinstance(userData.get("name"), str) or not userData["name"].strip():
        
        logger.warning(f"Requisição com name vazio")
        return jsonify(asdict(RequestResponse(
            hasError=True,
            message="name deve ser uma string não vazia!",
            statusCode=400
        ))), 400
    
    userData["email"] = userData["email"].strip()
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not isinstance(userData["email"], str) or not re.match(email_regex, userData["email"]):
        
        logger.warning(f"Requisição com email invalido")
        return jsonify(asdict(RequestResponse(
            hasError=True,
            message="email deve estar em formato válido!",
            statusCode=400
        ))), 400
    
    try:
        userData["roleId"] = int(userData["roleId"])
    except:
        logger.warning(f"Requisição com roleId sem ser um numero inteiro")
        return jsonify(asdict(RequestResponse(hasError=True, message=f"roleId deve ser um numero inteiro!", statusCode=400))),400
    
    try:  
        userService = UserService()
        logger.debug(f"Criando objeto User")
        userData = User(name = userData["name"], email = userData["email"], role_id = userData["roleId"], password = userData["password"])
        user : User = userService.createUser(userData)
        return jsonify(asdict(RequestResponse(message=f"Usuario {user.id} criado!"))), 200
    except ValueError as e:
        logger.error(str(e))
        return jsonify(asdict(RequestResponse(hasError=True, message=str(e), statusCode=404))),404
    except Exception as e:
        
        stacktrace = traceback.format_exc() 
        logger.error(f"Erro ao criar um usuario. Erro: {str(e)}. Stacktrace: {stacktrace}")
        return jsonify(asdict(RequestResponse(hasError=True, message=f"Ocorreu um erro durante a solicitação, por favor tente novamente!", statusCode=500))),500


@user_bp.route('/<userId>/getRoles', methods=['GET'])
def getRolesByUserId(userId):
    logger.info("Requisição para obter roles do usuario recebida")
    try:
        
        logger.info(f"Validando userId {userId}")
        userId = int(str(userId).strip())
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
            msg = f"Usuario {userId} não encontrado!"
            logger.info(msg)
            return jsonify(asdict(RequestResponse(message=msg))), 404
        return jsonify(asdict(RequestResponse(message=f"Roles do usuario {userId} encontrados!", data={"roles" : roles}))), 200
    except Exception as e:
        
        stacktrace = traceback.format_exc() 
        print(f"Erro ao obter roles do usuario {userId}. Erro: {str(e)}. Stacktrace: {stacktrace}")
        return jsonify(asdict(RequestResponse(hasError=True, message=f"Ocorreu um erro durante a solicitação, por favor tente novamente!", statusCode=500))),500
    
