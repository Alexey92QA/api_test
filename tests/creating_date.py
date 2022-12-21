from datetime import datetime

now_date = datetime.utcnow().strftime("%Y-%m-%d")
stop_date = datetime(1900, 12, 4).strftime("%Y-%m-%d")
error_date = datetime.utcnow().strftime(
                "%b "
                "%d, "
                "%Y.")
