import pydantic


class AppSettings(pydantic.BaseSettings):
    redis_url = pydantic.RedisDsn(url="redis://localhost/", scheme="redis")
    redis_port: int = 6379
    backend_url: str = "https://api.cobralo.pe"
    admin_email: str = "bensamuel114@gmail.com"
    admin_password: str = "admin12345"
    pending_sms_path: str = "/calendario/delivery-jobs/sms-pendientes"
    pending_whatsapp_path: str = "/calendario/delivery-jobs/whatsapp-pendientes"

    class Config:  # type: ignore[misc]
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = AppSettings()
