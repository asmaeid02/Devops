if result and result.get("status") == "success":
        return jsonify({"message": result.get("message")}), 200
    else:
        return jsonify({"error": result.get("message", "An error occurred.")}), 500