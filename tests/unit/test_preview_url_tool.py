"""Tests for the note_get_preview_url MCP tool."""

from unittest.mock import AsyncMock, patch

import pytest

from note_mcp.models import Session


@pytest.mark.asyncio
async def test_tool_returns_direct_preview_url(mock_session: Session) -> None:
    """The tool returns a shareable URL for the requested draft key."""
    from note_mcp.server import note_get_preview_url

    with (
        patch("note_mcp.decorators._session_manager.load", return_value=mock_session),
        patch(
            "note_mcp.server.get_preview_access_token",
            new_callable=AsyncMock,
            return_value="preview-token",
        ) as get_token,
        patch(
            "note_mcp.server.build_preview_url",
            return_value="https://note.com/preview/n1234567890ab?prev_access_key=preview-token",
        ) as build_url,
    ):
        result = await note_get_preview_url("n1234567890ab")

    assert result == "https://note.com/preview/n1234567890ab?prev_access_key=preview-token"
    get_token.assert_awaited_once_with(mock_session, "n1234567890ab")
    build_url.assert_called_once_with("n1234567890ab", "preview-token")


@pytest.mark.asyncio
async def test_tool_requires_an_authenticated_session() -> None:
    """The tool does not issue a preview token without authentication."""
    from note_mcp.server import note_get_preview_url

    with patch("note_mcp.decorators._session_manager.load", return_value=None):
        result = await note_get_preview_url("n1234567890ab")

    assert "ログイン" in result
