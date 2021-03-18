import datetime

from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Pattern,
    Set,
    Tuple,
    TypeVar,
    Union,
)
from flask.wrappers import Response
from ckan.lib.pagination import Page
import ckan.lib.formatters as formatters
import ckan.model as model

from markupsafe import Markup

DEFAULT_FACET_NAMES: str
MARKDOWN_TAGS: Set[str]
MARKDOWN_ATTRIBUTES: Dict[str, List[str]]
LEGACY_ROUTE_NAMES: Dict[str, str]

T = TypeVar("T")
BaseHelper = Callable
Helper = TypeVar("Helper", bound=BaseHelper)

class HelperAttributeDict(dict):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getitem__(self, key: str) -> BaseHelper: ...

helper_functions: HelperAttributeDict

class literal(Markup):

    __slots__: Iterable[str]
    @classmethod
    def escape(cls, s: Optional[str]) -> Markup: ...

def core_helper(f: Helper, name: Optional[str] = ...) -> Helper: ...
def chained_helper(func: Helper) -> Helper: ...
@core_helper
def redirect_to(*args: Any, **kw: Any) -> Response: ...
@core_helper
def get_site_protocol_and_host() -> Union[
    Tuple[str, str], Tuple[None, None]
]: ...
@core_helper
def url_for(*args: Any, **kw: Any) -> str: ...
@core_helper
def url_for_static(*args: Any, **kw: Any) -> str: ...
@core_helper
def url_for_static_or_external(*args: Any, **kw: Any) -> str: ...
@core_helper
def is_url(*args: Any, **kw: Any) -> bool: ...
@core_helper
def url_is_local(url: str) -> bool: ...
@core_helper
def full_current_url() -> str: ...
@core_helper
def current_url() -> str: ...
@core_helper
def lang() -> Optional[str]: ...
@core_helper
def ckan_version() -> str: ...
@core_helper
def lang_native_name(lang: Optional[str] = ...) -> str: ...
@core_helper
def is_rtl_language() -> bool: ...
@core_helper
def get_rtl_css() -> str: ...

class Message(object):
    category: str
    message: str
    allow_html: bool
    def __init__(
        self, category: str, message: str, allow_html: bool
    ) -> None: ...
    def __str__(self) -> str: ...
    def __html__(self) -> Union[Markup, str]: ...

class _Flash(object):
    categories: List[str] = ...
    default_category: str = ...
    def __init__(
        self,
        session_key: str = ...,
        categories: Optional[List[str]] = ...,
        default_category: Optional[str] = ...,
    ) -> None: ...
    def __call__(
        self,
        message: str,
        category: Optional[str] = ...,
        ignore_duplicate: bool = ...,
        allow_html: bool = ...,
    ) -> None: ...
    def pop_messages(self) -> List[Message]: ...
    def are_there_messages(self) -> bool: ...

flash: _Flash
@core_helper
def flash_notice(message: str, allow_html: bool = ...) -> None: ...
@core_helper
def flash_error(message: str, allow_html: bool = ...) -> None: ...
@core_helper
def flash_success(message: str, allow_html: bool = ...) -> None: ...
@core_helper
def are_there_flash_messages() -> bool: ...
@core_helper
def link_to(label: str, url: str, **attrs: Any) -> Markup: ...
@core_helper
def nav_link(text: str, *args: Any, **kwargs: Any) -> Union[Markup, str]: ...
@core_helper
def build_nav_main(
    *args: Union[
        Tuple[str, str],
        Tuple[str, str, List[str]],
        Tuple[str, str, List[str], str],
    ]
) -> Markup: ...
@core_helper
def build_nav_icon(menu_item: str, title: str, **kw: Any) -> Markup: ...
@core_helper
def build_nav(menu_item: str, title: str, **kw: Any) -> Markup: ...
@core_helper
def build_extra_admin_nav() -> Markup: ...
@core_helper
def default_group_type(type_: str = ...) -> str: ...
@core_helper
def humanize_entity_type(
    entity_type: str, object_type: str, purpose: str
) -> str: ...
@core_helper
def get_facet_items_dict(
    facet: str,
    search_facets: Optional[Dict] = ...,
    limit: Optional[int] = ...,
    exclude_active: bool = ...,
) -> List[Dict]: ...
@core_helper
def has_more_facets(
    facet: str,
    search_facets: Dict,
    limit: Optional[int] = ...,
    exclude_active: bool = ...,
) -> bool: ...
@core_helper
def unselected_facet_items(facet: str, limit: int = ...) -> List[Dict]: ...
@core_helper
def get_param_int(name: str, default: int = ...) -> int: ...
@core_helper
def sorted_extras(
    package_extras: Dict,
    auto_clean: bool = ...,
    subs: Dict[str, str] = ...,
    exclude: List[str] = ...,
) -> List[Tuple[str, Any]]: ...
@core_helper
def check_access(action: str, data_dict: Optional[Dict] = ...) -> bool: ...
@core_helper
def linked_user(
    user: Union[str, model.User], maxlength: int = ..., avatar: int = ...
) -> Union[Markup, str]: ...
@core_helper
def group_name_to_title(name: str) -> str: ...
@core_helper
def truncate(
    text: str, length: int = ..., indicator: str = ..., whole_word: bool = ...
) -> str: ...
@core_helper
def markdown_extract(
    text: str, extract_length: int = ...
) -> Union[str, Markup]: ...
@core_helper
def icon_url(name: str) -> str: ...
@core_helper
def icon_html(
    url: str, alt: Optional[str] = ..., inline: bool = ...
) -> Markup: ...
@core_helper
def icon(
    name: str, alt: Optional[str] = ..., inline: bool = ...
) -> Markup: ...
@core_helper
def resource_icon(res: Dict) -> Markup: ...
@core_helper
def format_icon(_format: str) -> str: ...
@core_helper
def dict_list_reduce(
    list_: List[Dict[str, T]], key: str, unique: bool = ...
) -> List[T]: ...
@core_helper
def gravatar(
    email_hash: str, size: int = ..., default: Optional[str] = ...
) -> Markup: ...
@core_helper
def user_image(user_id: str, size: int = ...) -> Union[Markup, str]: ...
@core_helper
def pager_url(
    page: int, partial: Optional[str] = ..., **kwargs: Any
) -> str: ...
@core_helper
def get_page_number(
    params: Dict, key: str = ..., default: int = ...
) -> int: ...
@core_helper
def get_display_timezone() -> str: ...
@core_helper
def render_datetime(
    datetime_: datetime.datetime,
    date_format: Optional[str] = ...,
    with_hours: bool = ...,
    with_seconds: bool = ...,
) -> str: ...
@core_helper
def date_str_to_datetime(date_str: str) -> datetime.datetime: ...
@core_helper
def parse_rfc_2822_date(
    date_str: str, assume_utc: bool = ...
) -> Optional[datetime.datetime]: ...
@core_helper
def time_ago_from_timestamp(timestamp: int) -> str: ...
@core_helper
def button_attr(enable: bool, type: str = ...) -> str: ...
@core_helper
def dataset_display_name(
    package_or_package_dict: Union[Dict, model.Package]
) -> str: ...
@core_helper
def dataset_link(
    package_or_package_dict: Union[Dict, model.Package]
) -> Markup: ...
@core_helper
def resource_display_name(resource_dict: Dict) -> str: ...
@core_helper
def resource_link(
    resource_dict: Dict, package_id: str, package_type: str = ...
) -> Markup: ...
@core_helper
def tag_link(tag: Dict, package_type: str = ...) -> Markup: ...
@core_helper
def group_link(group: Dict) -> Markup: ...
@core_helper
def organization_link(organization: Dict) -> Markup: ...
@core_helper
def dump_json(obj: Any, **kw: Any) -> str: ...
@core_helper
def auto_log_message() -> str: ...
@core_helper
def activity_div(
    template: str,
    activity: Dict,
    actor: str,
    object: Optional[str] = ...,
    target: Optional[str] = ...,
) -> Markup: ...
@core_helper
def snippet(template_name: str, **kw: Any) -> str: ...
@core_helper
def convert_to_dict(object_type: str, objs: List[Any]) -> List[Dict]: ...
@core_helper
def follow_button(obj_type: str, obj_id: str) -> str: ...
@core_helper
def follow_count(obj_type: str, obj_id: str) -> int: ...
@core_helper
def add_url_param(
    alternative_url: Optional[str] = ...,
    controller: Optional[str] = ...,
    action: Optional[str] = ...,
    extras: Optional[Dict] = ...,
    new_params: Optional[Dict] = ...,
) -> str: ...
@core_helper
def remove_url_param(
    key: str,
    value: Optional[str] = ...,
    replace: Optional[str] = ...,
    controller: Optional[str] = ...,
    action: Optional[str] = ...,
    extras: Optional[Dict] = ...,
    alternative_url: Optional[str] = ...,
) -> str: ...
@core_helper
def debug_inspect(arg: Any) -> Markup: ...
@core_helper
def popular(
    type_: str, number: int, min: int = ..., title: Optional[str] = ...
) -> str: ...
@core_helper
def groups_available(am_member: bool = ...) -> List[Dict]: ...
@core_helper
def organizations_available(
    permission: str = ..., include_dataset_count: bool = ...
) -> List[Dict]: ...
@core_helper
def roles_translated() -> Dict[str, str]: ...
@core_helper
def user_in_org_or_group(group_id: str) -> bool: ...
@core_helper
def dashboard_activity_stream(
    user_id: str,
    filter_type: Optional[str] = ...,
    filter_id: Optional[str] = ...,
    offset: int = ...,
) -> List[Dict]: ...
@core_helper
def recently_changed_packages_activity_stream(
    limit: Optional[int] = ...,
) -> List[Dict]: ...
@core_helper
def escape_js(str_to_escape: str) -> str: ...
@core_helper
def get_pkg_dict_extra(
    pkg_dict: Dict, key: str, default: Optional[Any] = ...
) -> Any: ...
@core_helper
def get_request_param(
    parameter_name: str, default: Optional[Any] = ...
) -> Any: ...

RE_MD_GET_INNER_HTML: Pattern
RE_MD_INTERNAL_LINK: Pattern
RE_MD_EXTERNAL_LINK: Pattern
RE_MD_HTML_TAGS: Pattern
@core_helper
def html_auto_link(data: str) -> str: ...
@core_helper
def render_markdown(
    data: str, auto_link: bool = ..., allow_html: bool = ...
) -> Union[str, Markup]: ...
@core_helper
def format_resource_items(
    items: List[Tuple[str, Any]]
) -> List[Tuple[str, Any]]: ...
@core_helper
def resource_preview(resource: Dict, package: Dict) -> str: ...
@core_helper
def get_allowed_view_types(resource: Dict, package: Dict) -> List[Dict]: ...
@core_helper
def rendered_resource_view(
    resource_view: Dict, resource: Dict, package: Dict, embed: bool = ...
) -> Markup: ...
@core_helper
def view_resource_url(
    resource_view: Dict, resource: Dict, package: Dict, **kw: Any
) -> str: ...
@core_helper
def resource_view_is_filterable(resource_view: Dict) -> bool: ...
@core_helper
def resource_view_get_fields(resource: Dict) -> List["str"]: ...
@core_helper
def resource_view_is_iframed(resource_view: Dict) -> bool: ...
@core_helper
def resource_view_icon(resource_view: Dict) -> str: ...
@core_helper
def resource_view_display_preview(resource_view: Dict) -> bool: ...
@core_helper
def resource_view_full_page(resource_view: Dict) -> bool: ...
@core_helper
def remove_linebreaks(string: str) -> str: ...
@core_helper
def list_dict_filter(
    list_: List[Dict], search_field: str, output_field: str, value: Any
) -> Any: ...
@core_helper
def SI_number_span(number: int) -> Markup: ...

localised_number: Callable[[int], str]
localised_SI_number: Callable[[int], str]
localised_nice_date: Callable[
    [datetime.datetime, bool, bool, bool, Optional[str]], str
]
localised_filesize: Callable[[int], str]
@core_helper
def new_activities() -> Optional[int]: ...
@core_helper
def uploads_enabled() -> bool: ...
@core_helper
def get_featured_organizations(count: int = ...) -> List[Dict]: ...
@core_helper
def get_featured_groups(count: int = ...) -> List[Dict]: ...
@core_helper
def featured_group_org(
    items: List[str], get_action: str, list_action: str, count: int
) -> List[Dict]: ...
@core_helper
def get_site_statistics() -> Dict[str, int]: ...
@core_helper
def resource_formats() -> Dict[str, List[str]]: ...
@core_helper
def unified_resource_format(format: str) -> str: ...
@core_helper
def check_config_permission(permission: str) -> Union[List[str], bool]: ...
@core_helper
def get_organization(
    org: Optional[str] = ..., include_datasets: bool = ...
) -> Dict: ...
@core_helper
def license_options(
    existing_license_id: Optional[Tuple[str, str]] = ...
) -> List[Tuple[str, str]]: ...
@core_helper
def get_translated(data_dict: Dict, field: str) -> Union[str, Any]: ...
@core_helper
def facets() -> List[str]: ...
@core_helper
def mail_to(email_address: str, name: str) -> Markup: ...
@core_helper
def radio(selected: str, id: str, checked: bool) -> Markup: ...
@core_helper
def clean_html(html: str) -> str: ...
def load_plugin_helpers() -> None: ...
@core_helper
def sanitize_id(id_: str) -> str: ...
@core_helper
def compare_pkg_dicts(
    old: Dict, new: Dict, old_activity_id: str
) -> List[Dict]: ...
@core_helper
def activity_list_select(
    pkg_activity_list: List[Dict], current_activity_id: str
) -> List[Markup]: ...
@core_helper
def get_collaborators(package_id: str) -> List[Tuple[str, str]]: ...
@core_helper
def can_update_owner_org(
    package_dict: Dict, user_orgs: Optional[List[Dict]] = ...
) -> bool: ...
