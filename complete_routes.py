from collections import namedtuple

from autorun_routes_service import RoutesService

routes_service = RoutesService()

ROUTES = namedtuple("ROUTES", [
    "lymhurst_market__lymhurst_marketplace__lymhurst",
    "lymhurst_market__lymhurst__lymhurst_marketplace",

    "lymhurst__lymhurst_market__ferndell",
    "lymhurst__ferndell__lymhurst_market",

    "ferndell__lymhurst__willow_wood",
    "ferndell__willow_wood__lymhurst",

    "willow_wood__ferndell__spindlewood",
    "willow_wood__spindlewood__ferndell",

    "spindlewood__willow_wood__longshadow_plain",
    "spindlewood__longshadow_plain__willow_wood",

    "longshadow_plain__spindlewood__snapshaft_trough",
    "longshadow_plain__snapshaft_trough__spindlewood",

    "snapshaft_trough__longshadow_plain__lazygrass_plain",
    "snapshaft_trough__lazygrass_plain__longshadow_plain",

    "lazygrass_plain__snapshaft_trough__bridgewatch",
    "lazygrass_plain__bridgewatch__snapshaft_trough",

    "bridgewatch__lazygrass_plain__bridgewatch_market",
    "bridgewatch__bridgewatch_market__lazygrass_plain",

    "bridgewatch__lazygrass_plain__smoothfloor_cleft",
    "bridgewatch__smoothfloor_cleft__lazygrass_plain",

    "smoothfloor_cleft__bridgewatch__redstone_plain",
    "smoothfloor_cleft__redstone_plain__bridgewatch",

    "redstone_plain__smoothfloor_cleft__felniks_hill",
    "redstone_plain__felniks_hill__smoothfloor_cleft",

    "felniks_hill__redstone_plain__carns_hill",
    "felniks_hill__carns_hill__redstone_plain",

    "carns_hill__felniks_hill__adrens_hill",
    "carns_hill__adrens_hill__felniks_hill",

    "adrens_hill__carns_hill__blackthorn_quarry",
    "adrens_hill__blackthorn_quarry__carns_hill",

    "blackthorn_quarry__adrens_hill__martlock",
    "blackthorn_quarry__martlock__adrens_hill",

    "martlock__blackthorn_quarry__haytor",
    "martlock__haytor__blackthorn_quarry",

    "martlock__blackthorn_quarry__martlock_market",
    "martlock__martlock_market__blackthorn_quarry",
])

routes = ROUTES(**{
    "lymhurst_market__lymhurst_marketplace__lymhurst": routes_service.get_route('lymhurst_market__lymhurst_marketplace__lymhurst'),
    "lymhurst_market__lymhurst__lymhurst_marketplace": routes_service.reverse_route(routes_service.get_route('lymhurst_market__lymhurst_marketplace__lymhurst')),

    "lymhurst__lymhurst_market__ferndell": routes_service.get_route('lymhurst__lymhurst_market__ferndell'),
    "lymhurst__ferndell__lymhurst_market": routes_service.reverse_route(routes_service.get_route('lymhurst__lymhurst_market__ferndell')),

    "ferndell__lymhurst__willow_wood": routes_service.get_route('ferndell__lymhurst__willow_wood'),
    "ferndell__willow_wood__lymhurst": routes_service.reverse_route(routes_service.get_route('ferndell__lymhurst__willow_wood')),

    "willow_wood__ferndell__spindlewood": routes_service.get_route('willow_wood__ferndell__spindlewood'),
    "willow_wood__spindlewood__ferndell": routes_service.reverse_route(routes_service.get_route('willow_wood__ferndell__spindlewood')),

    "spindlewood__willow_wood__longshadow_plain": routes_service.get_route('spindlewood__willow_wood__longshadow_plain'),
    "spindlewood__longshadow_plain__willow_wood": routes_service.reverse_route(routes_service.get_route('spindlewood__willow_wood__longshadow_plain')),

    "longshadow_plain__spindlewood__snapshaft_trough": routes_service.get_route('longshadow_plain__spindlewood__snapshaft_trough'),
    "longshadow_plain__snapshaft_trough__spindlewood": routes_service.reverse_route(routes_service.get_route('longshadow_plain__spindlewood__snapshaft_trough')),

    "snapshaft_trough__longshadow_plain__lazygrass_plain": routes_service.get_route('snapshaft_trough__longshadow_plain__lazygrass_plain'),
    "snapshaft_trough__lazygrass_plain__longshadow_plain": routes_service.reverse_route(routes_service.get_route('snapshaft_trough__longshadow_plain__lazygrass_plain')),

    "lazygrass_plain__snapshaft_trough__bridgewatch": routes_service.get_route('lazygrass_plain__snapshaft_trough__bridgewatch'),
    "lazygrass_plain__bridgewatch__snapshaft_trough": routes_service.reverse_route(routes_service.get_route('lazygrass_plain__snapshaft_trough__bridgewatch')),

    "bridgewatch__lazygrass_plain__bridgewatch_market": routes_service.get_route('bridgewatch__lazygrass_plain__bridgewatch_market'),
    "bridgewatch__bridgewatch_market__lazygrass_plain": routes_service.reverse_route(routes_service.get_route( 'bridgewatch__lazygrass_plain__bridgewatch_market')),

    "bridgewatch__lazygrass_plain__smoothfloor_cleft": routes_service.get_route('bridgewatch__lazygrass_plain__smoothfloor_cleft'),
    "bridgewatch__smoothfloor_cleft__lazygrass_plain": routes_service.reverse_route(routes_service.get_route( 'bridgewatch__lazygrass_plain__smoothfloor_cleft')),

    "smoothfloor_cleft__bridgewatch__redstone_plain": routes_service.get_route('smoothfloor_cleft__bridgewatch__redstone_plain'),
    "smoothfloor_cleft__redstone_plain__bridgewatch": routes_service.reverse_route(routes_service.get_route('smoothfloor_cleft__bridgewatch__redstone_plain')),

    "redstone_plain__smoothfloor_cleft__felniks_hill": routes_service.get_route('redstone_plain__smoothfloor_cleft__felniks_hill'),
    "redstone_plain__felniks_hill__smoothfloor_cleft": routes_service.reverse_route(routes_service.get_route('redstone_plain__smoothfloor_cleft__felniks_hill')),

    "felniks_hill__redstone_plain__carns_hill": routes_service.get_route('felniks_hill__redstone_plain__carns_hill'),
    "felniks_hill__carns_hill__redstone_plain": routes_service.reverse_route(routes_service.get_route('felniks_hill__redstone_plain__carns_hill')),

    "carns_hill__felniks_hill__adrens_hill": routes_service.get_route('carns_hill__felniks_hill__adrens_hill'),
    "carns_hill__adrens_hill__felniks_hill": routes_service.reverse_route(routes_service.get_route('carns_hill__felniks_hill__adrens_hill')),

    "adrens_hill__carns_hill__blackthorn_quarry": routes_service.get_route('adrens_hill__carns_hill__blackthorn_quarry'),
    "adrens_hill__blackthorn_quarry__carns_hill": routes_service.reverse_route(routes_service.get_route('adrens_hill__carns_hill__blackthorn_quarry')),

    "blackthorn_quarry__adrens_hill__martlock": routes_service.get_route('blackthorn_quarry__adrens_hill__martlock'),
    "blackthorn_quarry__martlock__adrens_hill": routes_service.reverse_route(routes_service.get_route('blackthorn_quarry__adrens_hill__martlock')),

    "martlock__blackthorn_quarry__haytor": routes_service.get_route('martlock__blackthorn_quarry__haytor'),
    "martlock__haytor__blackthorn_quarry": routes_service.reverse_route(routes_service.get_route('martlock__blackthorn_quarry__haytor')),

    "martlock__blackthorn_quarry__martlock_market": routes_service.get_route('martlock__blackthorn_quarry__martlock_market'),
    "martlock__martlock_market__blackthorn_quarry": routes_service.reverse_route(routes_service.get_route('martlock__blackthorn_quarry__martlock_market')),
})


COMPLETE_ROUTES = namedtuple("COMPLETE_ROUTES", [
    "lymhurst__bridgewatch",
    "bridgewatch__martlock",

    "martlock__bridgewatch",
    "bridgewatch__lymhurst",
])

complete_routes = COMPLETE_ROUTES(**{
    "lymhurst__bridgewatch": [
        routes.lymhurst__lymhurst_market__ferndell,
        routes.ferndell__lymhurst__willow_wood,
        routes.willow_wood__ferndell__spindlewood,
        routes.spindlewood__willow_wood__longshadow_plain,
        routes.longshadow_plain__spindlewood__snapshaft_trough,
        routes.snapshaft_trough__longshadow_plain__lazygrass_plain,
        routes.lazygrass_plain__snapshaft_trough__bridgewatch,
    ],
    "bridgewatch__martlock": [routes.bridgewatch__bridgewatch_market__lazygrass_plain],

    "martlock__bridgewatch": [
        routes.martlock__martlock_market__blackthorn_quarry,
        routes.blackthorn_quarry__martlock__adrens_hill,
        routes.adrens_hill__blackthorn_quarry__carns_hill,
        routes.carns_hill__adrens_hill__felniks_hill,
        routes.felniks_hill__carns_hill__redstone_plain,
        routes.redstone_plain__felniks_hill__smoothfloor_cleft,
        routes.smoothfloor_cleft__redstone_plain__bridgewatch,
    ],
    "bridgewatch__lymhurst": [
        routes.bridgewatch__bridgewatch_market__lazygrass_plain,
        routes.lazygrass_plain__bridgewatch__snapshaft_trough,
        routes.snapshaft_trough__lazygrass_plain__longshadow_plain,
        routes.longshadow_plain__snapshaft_trough__spindlewood,
        routes.spindlewood__longshadow_plain__willow_wood,
        routes.willow_wood__spindlewood__ferndell,
        routes.ferndell__willow_wood__lymhurst,
    ],
})
