import collections


# CreateResponseMetadata is reserved for future use.
class CreateResponseMetadata:
    __slots__ = []
    def __init__(self):
        pass
    def __repr__(self):
        return '<sdm.CreateResponseMetadata>'.format()

# GetResponseMetadata is reserved for future use.
class GetResponseMetadata:
    __slots__ = []
    def __init__(self):
        pass
    def __repr__(self):
        return '<sdm.GetResponseMetadata>'.format()

# UpdateResponseMetadata is reserved for future use.
class UpdateResponseMetadata:
    __slots__ = []
    def __init__(self):
        pass
    def __repr__(self):
        return '<sdm.UpdateResponseMetadata>'.format()

# DeleteResponseMetadata is reserved for future use.
class DeleteResponseMetadata:
    __slots__ = []
    def __init__(self):
        pass
    def __repr__(self):
        return '<sdm.DeleteResponseMetadata>'.format()

# RateLimitMetadata contains information about remaining requests avaialable
# to the user over some timeframe.
# limit: How many total requests the user/token is authorized to make before being
# rate limited.
# remaining: How many remaining requests out of the limit are still avaialable.
# reset_at: The time when remaining will be reset to limit.
# bucket: The bucket this user/token is associated with, which may be shared between
# multiple users/tokens.
class RateLimitMetadata:
    __slots__ = ['limit', 'remaining', 'reset_at', 'bucket']
    def __init__(self):
        self.limit = None
        self.remaining = None
        self.reset_at = None
        self.bucket = None
    def __repr__(self):
        return '<sdm.RateLimitMetadata limit: {0} remaining: {1} reset_at: {2} bucket: {3}>'.format(repr(self.limit), repr(self.remaining), repr(self.reset_at), repr(self.bucket))

# NodeCreateResponse reports how the Nodes were created in the system.
# meta: Reserved for future use.
# node: The created Node.
# token: The auth token generated for the Node. The Node will use this token to
# authenticate with the strongDM API.
# rate_limit: Rate limit information.
class NodeCreateResponse:
    __slots__ = ['meta', 'node', 'token', 'rate_limit']
    def __init__(self):
        self.meta = None
        self.node = None
        self.token = None
        self.rate_limit = None
    def __repr__(self):
        return '<sdm.NodeCreateResponse meta: {0} node: {1} token: {2} rate_limit: {3}>'.format(repr(self.meta), repr(self.node), repr(self.token), repr(self.rate_limit))

# NodeGetResponse returns a requested Node.
# meta: Reserved for future use.
# node: The requested Node.
# rate_limit: Rate limit information.
class NodeGetResponse:
    __slots__ = ['meta', 'node', 'rate_limit']
    def __init__(self):
        self.meta = None
        self.node = None
        self.rate_limit = None
    def __repr__(self):
        return '<sdm.NodeGetResponse meta: {0} node: {1} rate_limit: {2}>'.format(repr(self.meta), repr(self.node), repr(self.rate_limit))

# NodeUpdateResponse returns the fields of a Node after it has been updated by
# a NodeUpdateRequest.
# meta: Reserved for future use.
# node: The updated Node.
# rate_limit: Rate limit information.
class NodeUpdateResponse:
    __slots__ = ['meta', 'node', 'rate_limit']
    def __init__(self):
        self.meta = None
        self.node = None
        self.rate_limit = None
    def __repr__(self):
        return '<sdm.NodeUpdateResponse meta: {0} node: {1} rate_limit: {2}>'.format(repr(self.meta), repr(self.node), repr(self.rate_limit))

# NodeDeleteResponse returns information about a Node that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class NodeDeleteResponse:
    __slots__ = ['meta', 'rate_limit']
    def __init__(self):
        self.meta = None
        self.rate_limit = None
    def __repr__(self):
        return '<sdm.NodeDeleteResponse meta: {0} rate_limit: {1}>'.format(repr(self.meta), repr(self.rate_limit))

# Relay represents a StrongDM CLI installation running in relay mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the relay. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
class Relay:
    __slots__ = ['id', 'name', 'state']
    def __init__(self):
        self.id = None
        self.name = None
        self.state = None
    def __repr__(self):
        return '<sdm.Relay id: {0} name: {1} state: {2}>'.format(repr(self.id), repr(self.name), repr(self.state))

# Gateway represents a StrongDM CLI installation running in gateway mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the gateway. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
# listen_address: The public hostname/port tuple at which the gateway will be accessible to clients.
# bind_address: The hostname/port tuple which the gateway daemon will bind to.
class Gateway:
    __slots__ = ['id', 'name', 'state', 'listen_address', 'bind_address']
    def __init__(self):
        self.id = None
        self.name = None
        self.state = None
        self.listen_address = None
        self.bind_address = None
    def __repr__(self):
        return '<sdm.Gateway id: {0} name: {1} state: {2} listen_address: {3} bind_address: {4}>'.format(repr(self.id), repr(self.name), repr(self.state), repr(self.listen_address), repr(self.bind_address))

# RoleCreateResponse reports how the Roles were created in the system. It can
# communicate partial successes or failures.
# meta: Reserved for future use.
# role: The created Role.
# rate_limit: Rate limit information.
class RoleCreateResponse:
    __slots__ = ['meta', 'role', 'rate_limit']
    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None
    def __repr__(self):
        return '<sdm.RoleCreateResponse meta: {0} role: {1} rate_limit: {2}>'.format(repr(self.meta), repr(self.role), repr(self.rate_limit))

# RoleGetResponse returns a requested Role.
# meta: Reserved for future use.
# role: The requested Role.
# rate_limit: Rate limit information.
class RoleGetResponse:
    __slots__ = ['meta', 'role', 'rate_limit']
    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None
    def __repr__(self):
        return '<sdm.RoleGetResponse meta: {0} role: {1} rate_limit: {2}>'.format(repr(self.meta), repr(self.role), repr(self.rate_limit))

# RoleUpdateResponse returns the fields of a Role after it has been updated by
# a RoleUpdateRequest.
# meta: Reserved for future use.
# role: The updated Role.
# rate_limit: Rate limit information.
class RoleUpdateResponse:
    __slots__ = ['meta', 'role', 'rate_limit']
    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None
    def __repr__(self):
        return '<sdm.RoleUpdateResponse meta: {0} role: {1} rate_limit: {2}>'.format(repr(self.meta), repr(self.role), repr(self.rate_limit))

# RoleDeleteResponse returns information about a Role that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleDeleteResponse:
    __slots__ = ['meta', 'rate_limit']
    def __init__(self):
        self.meta = None
        self.rate_limit = None
    def __repr__(self):
        return '<sdm.RoleDeleteResponse meta: {0} rate_limit: {1}>'.format(repr(self.meta), repr(self.rate_limit))

# A Role grants users access to a set of resources. Composite roles have no
# resource associations of their own, but instead grant access to the combined
# resources of their child roles.
# id: Unique identifier of the Role.
# name: Unique human-readable name of the Role.
# composite: True if the Role is a composite role.
class Role:
    __slots__ = ['id', 'name', 'composite']
    def __init__(self):
        self.id = None
        self.name = None
        self.composite = None
    def __repr__(self):
        return '<sdm.Role id: {0} name: {1} composite: {2}>'.format(repr(self.id), repr(self.name), repr(self.composite))
