# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

import openai._legacy_response as _legacy_response
from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import FileObject, FileDeleted
from openai._client import OpenAI, AsyncOpenAI
from openai.pagination import SyncPage, AsyncPage

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestFiles:
    strict_client = OpenAI(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = OpenAI(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        file = client.files.create(
            file=b"raw file contents",
            purpose="fine-tune",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.files.with_raw_response.create(
            file=b"raw file contents",
            purpose="fine-tune",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.files.with_streaming_response.create(
            file=b"raw file contents",
            purpose="fine-tune",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        file = client.files.retrieve(
            "string",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.files.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.files.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        file = client.files.list()
        assert_matches_type(SyncPage[FileObject], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        file = client.files.list(
            purpose="string",
        )
        assert_matches_type(SyncPage[FileObject], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncPage[FileObject], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncPage[FileObject], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: OpenAI) -> None:
        file = client.files.delete(
            "string",
        )
        assert_matches_type(FileDeleted, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: OpenAI) -> None:
        response = client.files.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleted, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: OpenAI) -> None:
        with client.files.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_content(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = client.files.content(
            "string",
        )
        assert isinstance(file, _legacy_response.HttpxBinaryResponseContent)
        assert file.json() == {"foo": "bar"}

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_content(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = client.files.with_raw_response.content(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(_legacy_response.HttpxBinaryResponseContent, file, path=["response"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_content(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.files.with_streaming_response.content(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(bytes, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_content(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.content(
                "",
            )

    @parametrize
    def test_method_retrieve_content(self, client: OpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.files.retrieve_content(
                "string",
            )

        assert_matches_type(str, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve_content(self, client: OpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.files.with_raw_response.retrieve_content(
                "string",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(str, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_content(self, client: OpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.files.with_streaming_response.retrieve_content(
                "string",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_content(self, client: OpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                client.files.with_raw_response.retrieve_content(
                    "",
                )


class TestAsyncFiles:
    strict_client = AsyncOpenAI(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOpenAI(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOpenAI) -> None:
        file = await client.files.create(
            file=b"raw file contents",
            purpose="fine-tune",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncOpenAI) -> None:
        response = await client.files.with_raw_response.create(
            file=b"raw file contents",
            purpose="fine-tune",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncOpenAI) -> None:
        async with client.files.with_streaming_response.create(
            file=b"raw file contents",
            purpose="fine-tune",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncOpenAI) -> None:
        file = await client.files.retrieve(
            "string",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncOpenAI) -> None:
        response = await client.files.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncOpenAI) -> None:
        async with client.files.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncOpenAI) -> None:
        file = await client.files.list()
        assert_matches_type(AsyncPage[FileObject], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOpenAI) -> None:
        file = await client.files.list(
            purpose="string",
        )
        assert_matches_type(AsyncPage[FileObject], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncOpenAI) -> None:
        response = await client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(AsyncPage[FileObject], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncOpenAI) -> None:
        async with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncPage[FileObject], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, client: AsyncOpenAI) -> None:
        file = await client.files.delete(
            "string",
        )
        assert_matches_type(FileDeleted, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncOpenAI) -> None:
        response = await client.files.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleted, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, client: AsyncOpenAI) -> None:
        async with client.files.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_content(self, client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = await client.files.content(
            "string",
        )
        assert isinstance(file, _legacy_response.HttpxBinaryResponseContent)
        assert file.json() == {"foo": "bar"}

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_content(self, client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = await client.files.with_raw_response.content(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(_legacy_response.HttpxBinaryResponseContent, file, path=["response"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_content(self, client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with client.files.with_streaming_response.content(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(bytes, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_content(self, client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await client.files.with_raw_response.content(
                "",
            )

    @parametrize
    async def test_method_retrieve_content(self, client: AsyncOpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            file = await client.files.retrieve_content(
                "string",
            )

        assert_matches_type(str, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_content(self, client: AsyncOpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await client.files.with_raw_response.retrieve_content(
                "string",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(str, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_content(self, client: AsyncOpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            async with client.files.with_streaming_response.retrieve_content(
                "string",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_content(self, client: AsyncOpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                await client.files.with_raw_response.retrieve_content(
                    "",
                )
