from supabase import create_client, Client
from app.config import settings


def get_service_client() -> Client:
    """Service-role client for privileged backend writes.
    Never expose this key to the browser.
    """
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


def get_user_client(user_jwt: str) -> Client:
    """User-scoped client that forwards the authenticated user's JWT.
    All reads and writes are subject to RLS as that user.
    """
    client = create_client(settings.supabase_url, settings.supabase_anon_key)
    client.auth.set_session(access_token=user_jwt, refresh_token="")
    return client
