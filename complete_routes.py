from collections import namedtuple

from autorun_routes_service import RoutesService

routes_service = RoutesService()

ROUTES = namedtuple("ROUTES", [
    "ferndell__lymhurst__willow_wood",
    "ferndell__willow_wood__lymhurst__r",

    "willow_wood__ferndell__spindlewood",
    "willow_wood__spindlewood__ferndell__r",

    "spindlewood__willow_wood__longshadow_plain",
    "spindlewood__longshadow_plain__willow_wood__r",

    "longshadow_plain__spindlewood__snapshaft_trough",
    "longshadow_plain__snapshaft_trough__spindlewood__r",

    "snapshaft_trough__longshadow_plain__lazygrass_plain",
    "snapshaft_trough__lazygrass_plain__longshadow_plain__r",

    "lazygrass_plain__snapshaft_trough__bridgewatch",
    "lazygrass_plain__bridgewatch__snapshaft_trough__r",

    "smoothfloor_cleft__bridgewatch__redstone_plain",
    "smoothfloor_cleft__redstone_plain__bridgewatch__r",

    "redstone_plain__smoothfloor_cleft__felniks_hill",
    "redstone_plain__felniks_hill__smoothfloor_cleft__r",

    "felniks_hill__redstone_plain__carns_hill",
    "felniks_hill__carns_hill__redstone_plain__r",

    "carns_hill__felniks_hill__adrens_hill",
    "carns_hill__adrens_hill__felniks_hill__r",

    "adrens_hill__carns_hill__blackthorn_quarry",
    "adrens_hill__blackthorn_quarry__carns_hill__r",

    "blackthorn_quarry__adrens_hill__martlock",
    "blackthorn_quarry__martlock__adrens_hill__r",

    "spindlewood__longshadow_plain__goldshimmer_plain",
    "spindlewood__goldshimmer_plain__longshadow_plain__r",

    "goldshimmer_plain__spindlewood__deeproot_wood",
    "goldshimmer_plain__deeproot_wood__spindlewood__r",

    "deeproot_wood__goldshimmer_plain__hornbeam_wood",
    "deeproot_wood__hornbeam_wood__goldshimmer_plain__r",

    "hornbeam_wood__deeproot_wood__shady_thunder_heart_mission",
    "hornbeam_wood__shady_thunder_heart_mission__deeproot_wood__r",

])

routes = ROUTES(**{
    "ferndell__lymhurst__willow_wood": routes_service.get_route('ferndell__lymhurst__willow_wood'),
    "ferndell__willow_wood__lymhurst__r": routes_service.reverse_route(routes_service.get_route('ferndell__lymhurst__willow_wood')),

    "willow_wood__ferndell__spindlewood": routes_service.get_route('willow_wood__ferndell__spindlewood'),
    "willow_wood__spindlewood__ferndell__r": routes_service.reverse_route(routes_service.get_route('willow_wood__ferndell__spindlewood')),

    "spindlewood__willow_wood__longshadow_plain": routes_service.get_route('spindlewood__willow_wood__longshadow_plain'),
    "spindlewood__longshadow_plain__willow_wood__r": routes_service.reverse_route(routes_service.get_route('spindlewood__willow_wood__longshadow_plain')),

    "longshadow_plain__spindlewood__snapshaft_trough": routes_service.get_route('longshadow_plain__spindlewood__snapshaft_trough'),
    "longshadow_plain__snapshaft_trough__spindlewood__r": routes_service.reverse_route(routes_service.get_route('longshadow_plain__spindlewood__snapshaft_trough')),

    "snapshaft_trough__longshadow_plain__lazygrass_plain": routes_service.get_route('snapshaft_trough__longshadow_plain__lazygrass_plain'),
    "snapshaft_trough__lazygrass_plain__longshadow_plain__r": routes_service.reverse_route(routes_service.get_route('snapshaft_trough__longshadow_plain__lazygrass_plain')),

    "lazygrass_plain__snapshaft_trough__bridgewatch": routes_service.get_route('lazygrass_plain__snapshaft_trough__bridgewatch'),
    "lazygrass_plain__bridgewatch__snapshaft_trough__r": routes_service.reverse_route(routes_service.get_route('lazygrass_plain__snapshaft_trough__bridgewatch')),

    "smoothfloor_cleft__bridgewatch__redstone_plain": routes_service.get_route('smoothfloor_cleft__bridgewatch__redstone_plain'),
    "smoothfloor_cleft__redstone_plain__bridgewatch__r": routes_service.reverse_route(routes_service.get_route('smoothfloor_cleft__bridgewatch__redstone_plain')),

    "redstone_plain__smoothfloor_cleft__felniks_hill": routes_service.get_route('redstone_plain__smoothfloor_cleft__felniks_hill'),
    "redstone_plain__felniks_hill__smoothfloor_cleft__r": routes_service.reverse_route(routes_service.get_route('redstone_plain__smoothfloor_cleft__felniks_hill')),

    "felniks_hill__redstone_plain__carns_hill": routes_service.get_route('felniks_hill__redstone_plain__carns_hill'),
    "felniks_hill__carns_hill__redstone_plain__r": routes_service.reverse_route(routes_service.get_route('felniks_hill__redstone_plain__carns_hill')),

    "carns_hill__felniks_hill__adrens_hill": routes_service.get_route('carns_hill__felniks_hill__adrens_hill'),
    "carns_hill__adrens_hill__felniks_hill__r": routes_service.reverse_route(routes_service.get_route('carns_hill__felniks_hill__adrens_hill')),

    "adrens_hill__carns_hill__blackthorn_quarry": routes_service.get_route('adrens_hill__carns_hill__blackthorn_quarry'),
    "adrens_hill__blackthorn_quarry__carns_hill__r": routes_service.reverse_route(routes_service.get_route('adrens_hill__carns_hill__blackthorn_quarry')),

    "blackthorn_quarry__adrens_hill__martlock": routes_service.get_route('blackthorn_quarry__adrens_hill__martlock'),
    "blackthorn_quarry__martlock__adrens_hill__r": routes_service.reverse_route(routes_service.get_route('blackthorn_quarry__adrens_hill__martlock')),

    "spindlewood__longshadow_plain__goldshimmer_plain": routes_service.get_route('spindlewood__longshadow_plain__goldshimmer_plain'),
    "spindlewood__goldshimmer_plain__longshadow_plain__r": routes_service.reverse_route(routes_service.get_route('spindlewood__longshadow_plain__goldshimmer_plain')),

    "goldshimmer_plain__spindlewood__deeproot_wood": routes_service.get_route('goldshimmer_plain__spindlewood__deeproot_wood'),
    "goldshimmer_plain__deeproot_wood__spindlewood__r": routes_service.reverse_route(routes_service.get_route('goldshimmer_plain__spindlewood__deeproot_wood')),

    "deeproot_wood__goldshimmer_plain__hornbeam_wood": routes_service.get_route('deeproot_wood__goldshimmer_plain__hornbeam_wood'),
    "deeproot_wood__hornbeam_wood__goldshimmer_plain__r": routes_service.reverse_route(routes_service.get_route('deeproot_wood__goldshimmer_plain__hornbeam_wood')),

    "hornbeam_wood__deeproot_wood__shady_thunder_heart_mission": routes_service.get_route('hornbeam_wood__deeproot_wood__shady_thunder_heart_mission'),
    "hornbeam_wood__shady_thunder_heart_mission__deeproot_wood__r": routes_service.reverse_route(routes_service.get_route('hornbeam_wood__deeproot_wood__shady_thunder_heart_mission')),

})

CITY_ROUTES = namedtuple("CITY_ROUTES", [
    "lymhurst_market__lymhurst_marketplace__lymhurst",
    "lymhurst_market__lymhurst__lymhurst_marketplace__r",

    "lymhurst__lymhurst_market__ferndell",
    "lymhurst__ferndell__lymhurst_market__r",

    "bridgewatch__lazygrass_plain__bridgewatch_market",
    "bridgewatch__bridgewatch_market__lazygrass_plain__r",

    "bridgewatch__lazygrass_plain__smoothfloor_cleft",
    "bridgewatch__smoothfloor_cleft__lazygrass_plain__r",

    "bridgewatch__lazygrass_plain__bank_of_bridgewatch",
    "bridgewatch__bank_of_bridgewatch__lazygrass_plain__r",

    "bridgewatch__yara_sunblaze_heart_mission__bank_of_bridgewatch",
    "bridgewatch__bank_of_bridgewatch__yara_sunblaze_heart_mission__r",

    "bridgewatch__lazygrass_plain__yara_sunblaze_heart_mission",
    "bridgewatch__yara_sunblaze_heart_mission__lazygrass_plain__r",

    "bank_of_bridgewatch__bridgewatch__bank_chest",
    "bank_of_bridgewatch__bank_chest__bridgewatch__r",

    "martlock__blackthorn_quarry__haytor",
    "martlock__haytor__blackthorn_quarry__r",

    "martlock__blackthorn_quarry__martlock_market",
    "martlock__martlock_market__blackthorn_quarry__r",
])

city_routes = CITY_ROUTES(**{
    "lymhurst_market__lymhurst_marketplace__lymhurst": routes_service.get_route('lymhurst_market__lymhurst_marketplace__lymhurst'),
    "lymhurst_market__lymhurst__lymhurst_marketplace__r": routes_service.reverse_route(routes_service.get_route('lymhurst_market__lymhurst_marketplace__lymhurst')),

    "lymhurst__lymhurst_market__ferndell": routes_service.get_route('lymhurst__lymhurst_market__ferndell'),
    "lymhurst__ferndell__lymhurst_market__r": routes_service.reverse_route(routes_service.get_route('lymhurst__lymhurst_market__ferndell')),

    "bridgewatch__lazygrass_plain__bridgewatch_market": routes_service.get_route('bridgewatch__lazygrass_plain__bridgewatch_market'),
    "bridgewatch__bridgewatch_market__lazygrass_plain__r": routes_service.reverse_route(routes_service.get_route('bridgewatch__lazygrass_plain__bridgewatch_market')),

    "bridgewatch__lazygrass_plain__smoothfloor_cleft": routes_service.get_route('bridgewatch__lazygrass_plain__smoothfloor_cleft'),
    "bridgewatch__smoothfloor_cleft__lazygrass_plain__r": routes_service.reverse_route(routes_service.get_route( 'bridgewatch__lazygrass_plain__smoothfloor_cleft')),

    "bridgewatch__lazygrass_plain__bank_of_bridgewatch": routes_service.get_route('bridgewatch__lazygrass_plain__bank_of_bridgewatch'),
    "bridgewatch__bank_of_bridgewatch__lazygrass_plain__r": routes_service.reverse_route(routes_service.get_route('bridgewatch__lazygrass_plain__bank_of_bridgewatch')),

    "bridgewatch__yara_sunblaze_heart_mission__bank_of_bridgewatch": routes_service.get_route('bridgewatch__yara_sunblaze_heart_mission__bank_of_bridgewatch'),
    "bridgewatch__bank_of_bridgewatch__yara_sunblaze_heart_mission__r": routes_service.reverse_route(routes_service.get_route('bridgewatch__yara_sunblaze_heart_mission__bank_of_bridgewatch')),

    "bridgewatch__lazygrass_plain__yara_sunblaze_heart_mission": routes_service.get_route('bridgewatch__lazygrass_plain__yara_sunblaze_heart_mission'),
    "bridgewatch__yara_sunblaze_heart_mission__lazygrass_plain__r": routes_service.reverse_route(routes_service.get_route('bridgewatch__lazygrass_plain__yara_sunblaze_heart_mission')),

    "bank_of_bridgewatch__bridgewatch__bank_chest": routes_service.get_route('bank_of_bridgewatch__bridgewatch__bank_chest'),
    "bank_of_bridgewatch__bank_chest__bridgewatch__r": routes_service.reverse_route(routes_service.get_route('bank_of_bridgewatch__bridgewatch__bank_chest')),

    "martlock__blackthorn_quarry__martlock_market": routes_service.get_route('martlock__blackthorn_quarry__martlock_market'),
    "martlock__martlock_market__blackthorn_quarry__r": routes_service.reverse_route(routes_service.get_route('martlock__blackthorn_quarry__martlock_market')),

    "martlock__blackthorn_quarry__haytor": routes_service.get_route('martlock__blackthorn_quarry__haytor'),
    "martlock__haytor__blackthorn_quarry__r": routes_service.reverse_route(routes_service.get_route('martlock__blackthorn_quarry__haytor')),
})


COMPLETE_ROUTES = namedtuple("COMPLETE_ROUTES", [
    "lymhurst__bridgewatch",
    "bridgewatch__martlock",

    "martlock__bridgewatch",
    "bridgewatch__lymhurst",

    "bridgewatch__hornbeam_wood__treeheart_mission",
    "hornbeam_wood__bridgewatch__treeheart_mission",
])

complete_routes = COMPLETE_ROUTES(**{
    "lymhurst__bridgewatch": [
        city_routes.lymhurst__lymhurst_market__ferndell,
        routes.ferndell__lymhurst__willow_wood,
        routes.willow_wood__ferndell__spindlewood,
        routes.spindlewood__willow_wood__longshadow_plain,
        routes.longshadow_plain__spindlewood__snapshaft_trough,
        routes.snapshaft_trough__longshadow_plain__lazygrass_plain,
        routes.lazygrass_plain__snapshaft_trough__bridgewatch,
    ],
    "bridgewatch__martlock": [
        routes.smoothfloor_cleft__bridgewatch__redstone_plain,
        routes.redstone_plain__smoothfloor_cleft__felniks_hill,
        routes.felniks_hill__redstone_plain__carns_hill,
        routes.carns_hill__felniks_hill__adrens_hill,
        routes.adrens_hill__carns_hill__blackthorn_quarry,
        routes.blackthorn_quarry__adrens_hill__martlock
    ],

    "martlock__bridgewatch": [
        city_routes.martlock__martlock_market__blackthorn_quarry__r,
        routes.blackthorn_quarry__martlock__adrens_hill__r,
        routes.adrens_hill__blackthorn_quarry__carns_hill__r,
        routes.carns_hill__adrens_hill__felniks_hill__r,
        routes.felniks_hill__carns_hill__redstone_plain__r,
        routes.redstone_plain__felniks_hill__smoothfloor_cleft__r,
        routes.smoothfloor_cleft__redstone_plain__bridgewatch__r,
    ],
    "bridgewatch__lymhurst": [
        city_routes.bridgewatch__bridgewatch_market__lazygrass_plain__r,
        routes.lazygrass_plain__bridgewatch__snapshaft_trough__r,
        routes.snapshaft_trough__lazygrass_plain__longshadow_plain__r,
        routes.longshadow_plain__snapshaft_trough__spindlewood__r,
        routes.spindlewood__longshadow_plain__willow_wood__r,
        routes.willow_wood__spindlewood__ferndell__r,
        routes.ferndell__willow_wood__lymhurst__r,
    ],

    "bridgewatch__hornbeam_wood__treeheart_mission": [
        # city_routes.bank_of_bridgewatch__bank_chest__bridgewatch__r,
        routes.lazygrass_plain__bridgewatch__snapshaft_trough__r,
        routes.snapshaft_trough__lazygrass_plain__longshadow_plain__r,
        routes.longshadow_plain__snapshaft_trough__spindlewood__r,
        routes.spindlewood__longshadow_plain__goldshimmer_plain,
        routes.goldshimmer_plain__spindlewood__deeproot_wood,
        routes.deeproot_wood__goldshimmer_plain__hornbeam_wood,
        routes.hornbeam_wood__deeproot_wood__shady_thunder_heart_mission,
    ],
    "hornbeam_wood__bridgewatch__treeheart_mission": [
        routes.hornbeam_wood__shady_thunder_heart_mission__deeproot_wood__r,
        routes.deeproot_wood__hornbeam_wood__goldshimmer_plain__r,
        routes.goldshimmer_plain__deeproot_wood__spindlewood__r,
        routes.spindlewood__goldshimmer_plain__longshadow_plain__r,
        routes.longshadow_plain__spindlewood__snapshaft_trough,
        routes.snapshaft_trough__longshadow_plain__lazygrass_plain,
        routes.lazygrass_plain__snapshaft_trough__bridgewatch,
        # city_routes.bridgewatch__lazygrass_plain__bank_of_bridgewatch,
    ],
})
