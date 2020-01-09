from sqlalchemy import ARRAY, Boolean, Column, Date, DateTime, Enum, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Table, Text, text
from sqlalchemy.dialects.postgresql import TSVECTOR, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Abstract(Base):
    __tablename__ = 'abstracts'

    abstractid = Column(Integer, primary_key=True, server_default=text("nextval('abstracts_abstractid_seq'::regclass)"))
    abstract = Column(Text)
    html = Column(Text)


t_all_current_modules = Table(
    'all_current_modules', metadata,
    Column('module_ident', Integer),
    Column('moduleid', Text),
    Column('version', Text),
    Column('name', Text),
    Column('created', DateTime(True)),
    Column('revised', DateTime(True)),
    Column('abstractid', Integer),
    Column('licenseid', Integer),
    Column('doctype', Text),
    Column('submitter', Text),
    Column('submitlog', Text),
    Column('stateid', Integer),
    Column('parent', Integer),
    Column('language', Text),
    Column('authors', ARRAY(Text())),
    Column('maintainers', ARRAY(Text())),
    Column('licensors', ARRAY(Text())),
    Column('parentauthors', ARRAY(Text())),
    Column('portal_type', Text),
    Column('uuid', UUID),
    Column('major_version', Integer),
    Column('minor_version', Integer),
    Column('google_analytics', Text),
    Column('buylink', Text),
    Column('print_style', Text),
    Column('baked', DateTime(True)),
    Column('recipe', Integer)
)


t_all_modules = Table(
    'all_modules', metadata,
    Column('module_ident', Integer),
    Column('uuid', UUID),
    Column('portal_type', Text),
    Column('moduleid', Text),
    Column('version', Text),
    Column('name', Text),
    Column('created', DateTime(True)),
    Column('revised', DateTime(True)),
    Column('abstractid', Integer),
    Column('stateid', Integer),
    Column('doctype', Text),
    Column('licenseid', Integer),
    Column('submitter', Text),
    Column('submitlog', Text),
    Column('parent', Integer),
    Column('language', Text),
    Column('authors', ARRAY(Text())),
    Column('maintainers', ARRAY(Text())),
    Column('licensors', ARRAY(Text())),
    Column('parentauthors', ARRAY(Text())),
    Column('google_analytics', Text),
    Column('buylink', Text),
    Column('major_version', Integer),
    Column('minor_version', Integer),
    Column('print_style', Text)
)


class ApiKey(Base):
    __tablename__ = 'api_keys'

    id = Column(Integer, primary_key=True, server_default=text("nextval('api_keys_id_seq'::regclass)"))
    key = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    groups = Column(ARRAY(Text()))


t_current_modules = Table(
    'current_modules', metadata,
    Column('module_ident', Integer),
    Column('portal_type', Text),
    Column('moduleid', Text),
    Column('uuid', UUID),
    Column('version', Text),
    Column('name', Text),
    Column('created', DateTime(True)),
    Column('revised', DateTime(True)),
    Column('abstractid', Integer),
    Column('licenseid', Integer),
    Column('doctype', Text),
    Column('submitter', Text),
    Column('submitlog', Text),
    Column('stateid', Integer),
    Column('parent', Integer),
    Column('language', Text),
    Column('authors', ARRAY(Text())),
    Column('maintainers', ARRAY(Text())),
    Column('licensors', ARRAY(Text())),
    Column('parentauthors', ARRAY(Text())),
    Column('google_analytics', Text),
    Column('buylink', Text),
    Column('major_version', Integer),
    Column('minor_version', Integer),
    Column('print_style', Text),
    Column('baked', DateTime(True)),
    Column('recipe', Integer),
    Column('canonical', UUID)
)


class DocumentControl(Base):
    __tablename__ = 'document_controls'

    uuid = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    licenseid = Column(Integer)


class File(Base):
    __tablename__ = 'files'

    fileid = Column(Integer, primary_key=True, server_default=text("nextval('files_fileid_seq'::regclass)"))
    md5 = Column(Text, index=True)
    sha1 = Column(Text, unique=True)
    file = Column(LargeBinary)
    media_type = Column(Text)


class Keyword(Base):
    __tablename__ = 'keywords'

    keywordid = Column(Integer, primary_key=True, server_default=text("nextval('keywords_keywordid_seq'::regclass)"))
    word = Column(Text, nullable=False, index=True)

    modules = relationship('Module', secondary='modulekeywords')


t_latest_modules = Table(
    'latest_modules', metadata,
    Column('module_ident', Integer, index=True),
    Column('portal_type', Text, index=True),
    Column('moduleid', Text, index=True),
    Column('uuid', UUID, nullable=False, unique=True),
    Column('version', Text),
    Column('name', Text, nullable=False),
    Column('created', DateTime(True), nullable=False),
    Column('revised', DateTime(True), nullable=False),
    Column('abstractid', Integer),
    Column('licenseid', Integer, nullable=False),
    Column('doctype', Text, nullable=False),
    Column('submitter', Text),
    Column('submitlog', Text),
    Column('stateid', Integer, server_default=text("1")),
    Column('parent', Integer),
    Column('language', Text),
    Column('authors', ARRAY(Text()), index=True),
    Column('maintainers', ARRAY(Text())),
    Column('licensors', ARRAY(Text())),
    Column('parentauthors', ARRAY(Text())),
    Column('google_analytics', Text),
    Column('buylink', Text),
    Column('major_version', Integer),
    Column('minor_version', Integer),
    Column('print_style', Text),
    Column('baked', DateTime(True)),
    Column('recipe', Integer),
    Column('canonical', UUID)
)


class License(Base):
    __tablename__ = 'licenses'

    licenseid = Column(Integer, primary_key=True, server_default=text("nextval('licenses_licenseid_seq'::regclass)"))
    code = Column(Text)
    version = Column(Text)
    name = Column(Text)
    url = Column(Text)
    is_valid_for_publication = Column(Boolean, server_default=text("false"))


t_modulecounts = Table(
    'modulecounts', metadata,
    Column('countdate', Date),
    Column('modcount', Integer)
)


t_moduleoptionalroles = Table(
    'moduleoptionalroles', metadata,
    Column('module_ident', Integer),
    Column('roleid', Integer),
    Column('personids', ARRAY(Text()))
)


class Modulestate(Base):
    __tablename__ = 'modulestates'

    stateid = Column(Integer, primary_key=True, server_default=text("nextval('modulestates_stateid_seq'::regclass)"))
    statename = Column(Text)


class OverallHitRank(Base):
    __tablename__ = 'overall_hit_ranks'

    document = Column(UUID, primary_key=True)
    hits = Column(Integer, server_default=text("0"))
    average = Column(Float(53))
    rank = Column(Integer)


class PendingResource(Base):
    __tablename__ = 'pending_resources'

    id = Column(Integer, primary_key=True, server_default=text("nextval('pending_resources_id_seq'::regclass)"))
    data = Column(LargeBinary)
    hash = Column(Text, unique=True)
    md5 = Column(Text)
    media_type = Column(Text, nullable=False)
    exists_in_archive = Column(Boolean, server_default=text("false"))
    filename = Column(Text)


class Person(Base):
    __tablename__ = 'persons'

    personid = Column(Text, primary_key=True)
    honorific = Column(Text)
    firstname = Column(Text)
    othername = Column(Text)
    surname = Column(Text)
    lineage = Column(Text)
    fullname = Column(Text)
    email = Column(Text)
    homepage = Column(Text)
    comment = Column(Text)
    passwd = Column(LargeBinary)
    groups = Column(ARRAY(Text()))


class Publication(Base):
    __tablename__ = 'publications'

    id = Column(Integer, primary_key=True, server_default=text("nextval('publications_id_seq'::regclass)"))
    created = Column(DateTime(True), server_default=text("now()"))
    publisher = Column(Text, nullable=False)
    publication_message = Column(Text, nullable=False)
    epub = Column(LargeBinary)
    is_pre_publication = Column(Boolean, server_default=text("false"))
    state = Column(Enum('Done/Success', 'Publishing', 'Processing', 'Waiting for acceptance', 'Failed/Error', 'Waiting for moderation', 'Rejected', name='publication_states'), server_default=text("'Processing'::publication_states"))
    state_messages = Column(JSON)


class RecentHitRank(Base):
    __tablename__ = 'recent_hit_ranks'

    document = Column(UUID, primary_key=True)
    hits = Column(Integer, server_default=text("0"))
    average = Column(Float(53))
    rank = Column(Integer)


class Role(Base):
    __tablename__ = 'roles'

    roleid = Column(Integer, primary_key=True, server_default=text("nextval('roles_roleid_seq'::regclass)"))
    roleparam = Column(Text)
    rolename = Column(Text)
    roledisplayname = Column(Text)
    roleattribution = Column(Text)
    rolecomment = Column(Text)


class ServiceState(Base):
    __tablename__ = 'service_states'

    id = Column(Integer, primary_key=True, server_default=text("nextval('service_states_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    default_priority = Column(Integer, nullable=False)
    default_message = Column(Text, nullable=False)


t_similarities = Table(
    'similarities', metadata,
    Column('objectid', Text),
    Column('version', Text),
    Column('sims', ARRAY(Text())),
    Index('similarities_objectid_version_idx', 'objectid', 'version', unique=True)
)


class Tag(Base):
    __tablename__ = 'tags'

    tagid = Column(Integer, primary_key=True, server_default=text("nextval('tags_tagid_seq'::regclass)"))
    tag = Column(Text)
    scheme = Column(Text)


class Tree(Base):
    __tablename__ = 'trees'
    __table_args__ = (
        Index('trees_unique_doc_idx', 'documentid', 'is_collated', unique=True),
    )

    nodeid = Column(Integer, primary_key=True, server_default=text("nextval('nodeid_seq'::regclass)"))
    parent_id = Column(ForeignKey('trees.nodeid', ondelete='CASCADE'))
    documentid = Column(Integer, index=True)
    title = Column(Text)
    childorder = Column(Integer)
    latest = Column(Boolean)
    is_collated = Column(Boolean, server_default=text("false"))
    slug = Column(Text)

    parent = relationship('Tree', remote_side=[nodeid])


class User(Base):
    __tablename__ = 'users'

    username = Column(Text, primary_key=True)
    created = Column(DateTime(True), nullable=False, server_default=text("now()"))
    updated = Column(DateTime(True), nullable=False, server_default=text("now()"))
    first_name = Column(Text)
    last_name = Column(Text)
    full_name = Column(Text)
    suffix = Column(Text)
    title = Column(Text)
    is_moderated = Column(Boolean)


class DefaultPrintStyleRecipe(Base):
    __tablename__ = 'default_print_style_recipes'

    print_style = Column(Text, primary_key=True)
    tag = Column(Text)
    fileid = Column(ForeignKey('files.fileid'))
    recipe_type = Column(Text)
    revised = Column(DateTime(True), nullable=False)
    title = Column(Text)
    commit_id = Column(Text)

    file = relationship('File')


class DocumentAcl(Base):
    __tablename__ = 'document_acl'

    uuid = Column(ForeignKey('document_controls.uuid'), primary_key=True, nullable=False)
    user_id = Column(Text, primary_key=True, nullable=False)
    permission = Column(Enum('publish', name='permission_type'), primary_key=True, nullable=False)

    document_control = relationship('DocumentControl')


class LicenseAcceptance(Base):
    __tablename__ = 'license_acceptances'

    uuid = Column(ForeignKey('document_controls.uuid'), primary_key=True, nullable=False)
    user_id = Column(Text, primary_key=True, nullable=False)
    accepted = Column(Boolean)
    notified = Column(DateTime(True))

    document_control = relationship('DocumentControl')


class Module(Base):
    __tablename__ = 'modules'

    module_ident = Column(Integer, primary_key=True, server_default=text("nextval('modules_module_ident_seq'::regclass)"))
    portal_type = Column(Text, index=True)
    moduleid = Column(Text, index=True)
    uuid = Column(UUID, index=True)
    version = Column(Text)
    name = Column(Text, nullable=False)
    created = Column(DateTime(True), nullable=False, server_default=text("now()"))
    revised = Column(DateTime(True), nullable=False, server_default=text("now()"))
    abstractid = Column(ForeignKey('abstracts.abstractid', deferrable=True))
    licenseid = Column(ForeignKey('licenses.licenseid', deferrable=True), nullable=False)
    doctype = Column(Text, nullable=False)
    submitter = Column(Text)
    submitlog = Column(Text)
    stateid = Column(ForeignKey('modulestates.stateid', deferrable=True), server_default=text("1"))
    parent = Column(ForeignKey('modules.module_ident', deferrable=True))
    language = Column(Text)
    authors = Column(ARRAY(Text()))
    maintainers = Column(ARRAY(Text()))
    licensors = Column(ARRAY(Text()))
    parentauthors = Column(ARRAY(Text()))
    google_analytics = Column(Text)
    buylink = Column(Text)
    major_version = Column(Integer, server_default=text("1"))
    minor_version = Column(Integer)
    print_style = Column(Text)
    baked = Column(DateTime(True))
    recipe = Column(ForeignKey('files.fileid', deferrable=True))
    canonical = Column(UUID)

    abstract = relationship('Abstract')
    license = relationship('License')
    parent1 = relationship('Module', remote_side=[module_ident])
    file = relationship('File')
    modulestate = relationship('Modulestate')
    tags = relationship('Tag', secondary='moduletags')


class PendingDocument(Base):
    __tablename__ = 'pending_documents'

    id = Column(Integer, primary_key=True, server_default=text("nextval('pending_documents_id_seq'::regclass)"))
    publication_id = Column(ForeignKey('publications.id'), nullable=False)
    uuid = Column(ForeignKey('document_controls.uuid'), nullable=False)
    major_version = Column(Integer)
    minor_version = Column(Integer)
    type = Column(Enum('Document', 'Binder', name='document_types'), nullable=False)
    metadata_ = Column('metadata', JSON)
    content = Column(LargeBinary)
    license_accepted = Column(Boolean, server_default=text("false"))
    roles_accepted = Column(Boolean, server_default=text("false"))

    publication = relationship('Publication')
    document_control = relationship('DocumentControl')
    resources = relationship('PendingResource', secondary='pending_resource_associations')


class PrintStyleRecipe(Base):
    __tablename__ = 'print_style_recipes'

    print_style = Column(Text, primary_key=True, nullable=False)
    tag = Column(Text, primary_key=True, nullable=False)
    fileid = Column(ForeignKey('files.fileid'))
    recipe_type = Column(Text, server_default=text("'web'::text"))
    revised = Column(DateTime(True), nullable=False, server_default=text("now()"))
    title = Column(Text)
    commit_id = Column(Text)

    file = relationship('File')


class RoleAcceptance(Base):
    __tablename__ = 'role_acceptances'

    uuid = Column(ForeignKey('document_controls.uuid'), primary_key=True, nullable=False)
    user_id = Column(Text, primary_key=True, nullable=False)
    role_type = Column(Enum('Author', 'Copyright Holder', 'Editor', 'Illustrator', 'Publisher', 'Translator', name='role_types'), primary_key=True, nullable=False)
    accepted = Column(Boolean)
    notified = Column(DateTime(True))

    document_control = relationship('DocumentControl')


class ServiceStateMessage(Base):
    __tablename__ = 'service_state_messages'

    id = Column(Integer, primary_key=True, server_default=text("nextval('service_state_messages_id_seq'::regclass)"))
    service_state_id = Column(ForeignKey('service_states.id'))
    starts = Column(DateTime(True), nullable=False, server_default=text("now()"))
    ends = Column(DateTime(True), nullable=False, server_default=text("(now() + '02:00:00'::interval)"))
    priority = Column(Integer)
    message = Column(Text)

    service_state = relationship('ServiceState')


class CollatedFileAssociation(Base):
    __tablename__ = 'collated_file_associations'

    context = Column(ForeignKey('modules.module_ident', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    item = Column(ForeignKey('modules.module_ident', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    fileid = Column(ForeignKey('files.fileid', ondelete='CASCADE'))

    module = relationship('Module', primaryjoin='CollatedFileAssociation.context == Module.module_ident')
    file = relationship('File')
    module1 = relationship('Module', primaryjoin='CollatedFileAssociation.item == Module.module_ident')


class CollatedFti(Base):
    __tablename__ = 'collated_fti'

    item = Column(ForeignKey('modules.module_ident', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    context = Column(ForeignKey('modules.module_ident', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    module_idx = Column(TSVECTOR, index=True)
    fulltext = Column(Text)

    module = relationship('Module', primaryjoin='CollatedFti.context == Module.module_ident')
    module1 = relationship('Module', primaryjoin='CollatedFti.item == Module.module_ident')


class DocumentBakingResultAssociation(Base):
    __tablename__ = 'document_baking_result_associations'

    module_ident = Column(ForeignKey('modules.module_ident', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    result_id = Column(UUID, primary_key=True, nullable=False)
    created = Column(DateTime(True), nullable=False, server_default=text("now()"))

    module = relationship('Module')


t_document_hits = Table(
    'document_hits', metadata,
    Column('documentid', ForeignKey('modules.module_ident', ondelete='CASCADE'), nullable=False, index=True),
    Column('start_timestamp', DateTime(True), nullable=False),
    Column('end_timestamp', DateTime(True), nullable=False),
    Column('hits', Integer, server_default=text("0"))
)


t_module_files = Table(
    'module_files', metadata,
    Column('module_ident', ForeignKey('modules.module_ident', ondelete='CASCADE')),
    Column('fileid', ForeignKey('files.fileid')),
    Column('filename', Text),
    Index('module_files_idx', 'module_ident', 'filename', unique=True)
)


t_modulefti = Table(
    'modulefti', metadata,
    Column('module_ident', ForeignKey('modules.module_ident', ondelete='CASCADE'), unique=True),
    Column('module_idx', TSVECTOR, index=True),
    Column('fulltext', Text)
)


t_modulekeywords = Table(
    'modulekeywords', metadata,
    Column('module_ident', ForeignKey('modules.module_ident', ondelete='CASCADE', deferrable=True), nullable=False, index=True),
    Column('keywordid', ForeignKey('keywords.keywordid', deferrable=True), nullable=False, index=True),
    Index('modulekeywords_module_ident_keywordid_idx', 'module_ident', 'keywordid', unique=True)
)


t_moduleratings = Table(
    'moduleratings', metadata,
    Column('module_ident', ForeignKey('modules.module_ident'), index=True),
    Column('totalrating', Integer),
    Column('votes', Integer)
)


t_moduletags = Table(
    'moduletags', metadata,
    Column('module_ident', ForeignKey('modules.module_ident', ondelete='CASCADE', deferrable=True), index=True),
    Column('tagid', ForeignKey('tags.tagid', deferrable=True))
)


t_pending_resource_associations = Table(
    'pending_resource_associations', metadata,
    Column('document_id', ForeignKey('pending_documents.id'), primary_key=True, nullable=False),
    Column('resource_id', ForeignKey('pending_resources.id'), primary_key=True, nullable=False)
)
