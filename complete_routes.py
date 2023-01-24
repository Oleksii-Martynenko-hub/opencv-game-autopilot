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

    "birchcopse__flynsdell__lymhurst",
    "birchcopse__lymhurst__flynsdell__r",

    "cairn_camain__cairn_fidair__fort_sterling",
    "cairn_camain__fort_sterling__cairn_fidair__r",

    "cairn_fidair__cairn_gorm__cairn_camain",
    "cairn_fidair__cairn_camain__cairn_gorm__r",

    "cairn_glascore__sleetwater_basin__cairn_gorm",
    "cairn_glascore__cairn_gorm__sleetwater_basin__r",

    "falsestep_marsh__fog_fen__dusklight_fen",
    "falsestep_marsh__dusklight_fen__fog_fen__r",

    "haytor__martlock__curlew_fen",
    "haytor__curlew_fen__martlock__r",

    "curlew_fen__haytor__dewleaf_fen",
    "curlew_fen__dewleaf_fen__haytor__r",

    "dusklight_fen__falsestep_marsh__thetford",
    "dusklight_fen__thetford__falsestep_marsh__r",

    "cairn_gorm__cairn_glascore__cairn_fidair",
    "cairn_gorm__cairn_fidair__cairn_glascore__r",

    "fog_fen__dewleaf_fen__falsestep_marsh",
    "fog_fen__falsestep_marsh__dewleaf_fen__r",

    "flynsdell__oakcopse__birchcopse",
    "flynsdell__birchcopse__oakcopse__r",

    "dewleaf_fen__curlew_fen__fog_fen",
    "dewleaf_fen__fog_fen__curlew_fen__r",

    "mawar_gorge__fort_sterling__pen_kerrig",
    "mawar_gorge__pen_kerrig__fort_sterling__r",

    "oakcopse__rowanwood__aspenwood",
    "oakcopse__aspenwood__rowanwood__r",

    "oakcopse__rowanwood__flynsdell",
    "oakcopse__flynsdell__rowanwood__r",

    "pen_kerrig__mawar_gorge__rowanwood",
    "pen_kerrig__rowanwood__mawar_gorge__r",

    "rowanwood__pen_kerrig__oakcopse",
    "rowanwood__oakcopse__pen_kerrig__r",

    "sleetwater_basin__willowsigh_marsh__cairn_glascore",
    "sleetwater_basin__cairn_glascore__willowsigh_marsh__r",

    "willowsigh_marsh__thetford__sleetwater_basin",
    "willowsigh_marsh__sleetwater_basin__thetford__r",

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

    "birchcopse__flynsdell__lymhurst": routes_service.get_route('birchcopse__flynsdell__lymhurst'),
    "birchcopse__lymhurst__flynsdell__r": routes_service.reverse_route(routes_service.get_route('birchcopse__flynsdell__lymhurst')),

    "cairn_camain__cairn_fidair__fort_sterling": routes_service.get_route('cairn_camain__cairn_fidair__fort_sterling'),
    "cairn_camain__fort_sterling__cairn_fidair__r": routes_service.reverse_route(routes_service.get_route('cairn_camain__cairn_fidair__fort_sterling')),

    "cairn_fidair__cairn_gorm__cairn_camain": routes_service.get_route('cairn_fidair__cairn_gorm__cairn_camain'),
    "cairn_fidair__cairn_camain__cairn_gorm__r": routes_service.reverse_route(routes_service.get_route('cairn_fidair__cairn_gorm__cairn_camain')),

    "cairn_glascore__sleetwater_basin__cairn_gorm": routes_service.get_route('cairn_glascore__sleetwater_basin__cairn_gorm'),
    "cairn_glascore__cairn_gorm__sleetwater_basin__r": routes_service.reverse_route(routes_service.get_route('cairn_glascore__sleetwater_basin__cairn_gorm')),

    "falsestep_marsh__fog_fen__dusklight_fen": routes_service.get_route('falsestep_marsh__fog_fen__dusklight_fen'),
    "falsestep_marsh__dusklight_fen__fog_fen__r": routes_service.reverse_route(routes_service.get_route('falsestep_marsh__fog_fen__dusklight_fen')),

    "haytor__martlock__curlew_fen": routes_service.get_route('haytor__martlock__curlew_fen'),
    "haytor__curlew_fen__martlock__r": routes_service.reverse_route(routes_service.get_route('haytor__martlock__curlew_fen')),

    "curlew_fen__haytor__dewleaf_fen": routes_service.get_route('curlew_fen__haytor__dewleaf_fen'),
    "curlew_fen__dewleaf_fen__haytor__r": routes_service.reverse_route(routes_service.get_route('curlew_fen__haytor__dewleaf_fen')),

    "dusklight_fen__falsestep_marsh__thetford": routes_service.get_route('dusklight_fen__falsestep_marsh__thetford'),
    "dusklight_fen__thetford__falsestep_marsh__r": routes_service.reverse_route(routes_service.get_route('dusklight_fen__falsestep_marsh__thetford')),

    "cairn_gorm__cairn_glascore__cairn_fidair": routes_service.get_route('cairn_gorm__cairn_glascore__cairn_fidair'),
    "cairn_gorm__cairn_fidair__cairn_glascore__r": routes_service.reverse_route(routes_service.get_route('cairn_gorm__cairn_glascore__cairn_fidair')),

    "fog_fen__dewleaf_fen__falsestep_marsh": routes_service.get_route('fog_fen__dewleaf_fen__falsestep_marsh'),
    "fog_fen__falsestep_marsh__dewleaf_fen__r": routes_service.reverse_route(routes_service.get_route('fog_fen__dewleaf_fen__falsestep_marsh')),

    "flynsdell__oakcopse__birchcopse": routes_service.get_route('flynsdell__oakcopse__birchcopse'),
    "flynsdell__birchcopse__oakcopse__r": routes_service.reverse_route(routes_service.get_route('flynsdell__oakcopse__birchcopse')),

    "dewleaf_fen__curlew_fen__fog_fen": routes_service.get_route('dewleaf_fen__curlew_fen__fog_fen'),
    "dewleaf_fen__fog_fen__curlew_fen__r": routes_service.reverse_route(routes_service.get_route('dewleaf_fen__curlew_fen__fog_fen')),

    "mawar_gorge__fort_sterling__pen_kerrig": routes_service.get_route('mawar_gorge__fort_sterling__pen_kerrig'),
    "mawar_gorge__pen_kerrig__fort_sterling__r": routes_service.reverse_route(routes_service.get_route('mawar_gorge__fort_sterling__pen_kerrig')),

    "oakcopse__rowanwood__aspenwood": routes_service.get_route('oakcopse__rowanwood__aspenwood'),
    "oakcopse__aspenwood__rowanwood__r": routes_service.reverse_route(routes_service.get_route('oakcopse__rowanwood__aspenwood')),

    "oakcopse__rowanwood__flynsdell": routes_service.get_route('oakcopse__rowanwood__flynsdell'),
    "oakcopse__flynsdell__rowanwood__r": routes_service.reverse_route(routes_service.get_route('oakcopse__rowanwood__flynsdell')),

    "pen_kerrig__mawar_gorge__rowanwood": routes_service.get_route('pen_kerrig__mawar_gorge__rowanwood'),
    "pen_kerrig__rowanwood__mawar_gorge__r": routes_service.reverse_route(routes_service.get_route('pen_kerrig__mawar_gorge__rowanwood')),

    "rowanwood__pen_kerrig__oakcopse": routes_service.get_route('rowanwood__pen_kerrig__oakcopse'),
    "rowanwood__oakcopse__pen_kerrig__r": routes_service.reverse_route(routes_service.get_route('rowanwood__pen_kerrig__oakcopse')),

    "sleetwater_basin__willowsigh_marsh__cairn_glascore": routes_service.get_route('sleetwater_basin__willowsigh_marsh__cairn_glascore'),
    "sleetwater_basin__cairn_glascore__willowsigh_marsh__r": routes_service.reverse_route(routes_service.get_route('sleetwater_basin__willowsigh_marsh__cairn_glascore')),

    "willowsigh_marsh__thetford__sleetwater_basin": routes_service.get_route('willowsigh_marsh__thetford__sleetwater_basin'),
    "willowsigh_marsh__sleetwater_basin__thetford__r": routes_service.reverse_route(routes_service.get_route('willowsigh_marsh__thetford__sleetwater_basin')),
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

    "thetford__dusklight_fen__willowsigh_marsh",
    "thetford__willowsigh_marsh__dusklight_fen__r",

    "fort_sterling__cairn_camain__mawar_gorge",
    "fort_sterling__mawar_gorge__cairn_camain__r",

    "lymhurst__birchcopse__ferndell",
    "lymhurst__ferndell__birchcopse__r",

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

    "thetford__dusklight_fen__willowsigh_marsh": routes_service.get_route('thetford__dusklight_fen__willowsigh_marsh'),
    "thetford__willowsigh_marsh__dusklight_fen__r": routes_service.reverse_route(routes_service.get_route('thetford__dusklight_fen__willowsigh_marsh')),

    "fort_sterling__cairn_camain__mawar_gorge": routes_service.get_route('fort_sterling__cairn_camain__mawar_gorge'),
    "fort_sterling__mawar_gorge__cairn_camain__r": routes_service.reverse_route(routes_service.get_route('fort_sterling__cairn_camain__mawar_gorge')),

    "lymhurst__birchcopse__ferndell": routes_service.get_route('lymhurst__birchcopse__ferndell'),
    "lymhurst__ferndell__birchcopse__r": routes_service.reverse_route(routes_service.get_route('lymhurst__birchcopse__ferndell')),
})


COMPLETE_ROUTES = namedtuple("COMPLETE_ROUTES", [
    "bridgewatch__martlock",
    "bridgewatch__thetford",
    "bridgewatch__fort_sterling",
    "bridgewatch__lymhurst",

    "martlock__thetford",
    "martlock__fort_sterling",
    "martlock__lymhurst",
    "martlock__bridgewatch",

    "thetford__fort_sterling",
    "thetford__lymhurst",
    "thetford__bridgewatch",
    "thetford__martlock",

    "fort_sterling__lymhurst",
    "fort_sterling__bridgewatch",
    "fort_sterling__martlock",
    "fort_sterling__thetford",

    "lymhurst__bridgewatch",
    "lymhurst__martlock",
    "lymhurst__thetford",
    "lymhurst__fort_sterling",

    "bridgewatch__hornbeam_wood__treeheart_mission",
    "hornbeam_wood__bridgewatch__treeheart_mission",
])

complete_routes = COMPLETE_ROUTES(**{
    "bridgewatch__martlock": [
        city_routes.bridgewatch__lazygrass_plain__smoothfloor_cleft,

        routes.smoothfloor_cleft__bridgewatch__redstone_plain,
        routes.redstone_plain__smoothfloor_cleft__felniks_hill,
        routes.felniks_hill__redstone_plain__carns_hill,
        routes.carns_hill__felniks_hill__adrens_hill,
        routes.adrens_hill__carns_hill__blackthorn_quarry,
        routes.blackthorn_quarry__adrens_hill__martlock,
    ],
    "bridgewatch__thetford": [
        city_routes.bridgewatch__lazygrass_plain__smoothfloor_cleft,

        routes.smoothfloor_cleft__bridgewatch__redstone_plain,
        routes.redstone_plain__smoothfloor_cleft__felniks_hill,
        routes.felniks_hill__redstone_plain__carns_hill,
        routes.carns_hill__felniks_hill__adrens_hill,
        routes.adrens_hill__carns_hill__blackthorn_quarry,
        routes.blackthorn_quarry__adrens_hill__martlock,

        city_routes.martlock__blackthorn_quarry__haytor,

        routes.haytor__martlock__curlew_fen,
        routes.curlew_fen__haytor__dewleaf_fen,
        routes.dewleaf_fen__curlew_fen__fog_fen,
        routes.fog_fen__dewleaf_fen__falsestep_marsh,
        routes.falsestep_marsh__fog_fen__dusklight_fen,
        routes.dusklight_fen__falsestep_marsh__thetford,
    ],
    "bridgewatch__fort_sterling": [
        city_routes.bridgewatch__smoothfloor_cleft__lazygrass_plain__r,

        routes.lazygrass_plain__bridgewatch__snapshaft_trough__r,
        routes.snapshaft_trough__lazygrass_plain__longshadow_plain__r,
        routes.longshadow_plain__snapshaft_trough__spindlewood__r,
        routes.spindlewood__longshadow_plain__willow_wood__r,
        routes.willow_wood__spindlewood__ferndell__r,
        routes.ferndell__willow_wood__lymhurst__r,

        city_routes.lymhurst__ferndell__birchcopse__r,

        routes.birchcopse__lymhurst__flynsdell__r,
        routes.flynsdell__birchcopse__oakcopse__r,
        routes.oakcopse__flynsdell__rowanwood__r,
        routes.rowanwood__oakcopse__pen_kerrig__r,
        routes.pen_kerrig__rowanwood__mawar_gorge__r,
        routes.mawar_gorge__pen_kerrig__fort_sterling__r,
    ],
    "bridgewatch__lymhurst": [
        city_routes.bridgewatch__smoothfloor_cleft__lazygrass_plain__r,

        routes.lazygrass_plain__bridgewatch__snapshaft_trough__r,
        routes.snapshaft_trough__lazygrass_plain__longshadow_plain__r,
        routes.longshadow_plain__snapshaft_trough__spindlewood__r,
        routes.spindlewood__longshadow_plain__willow_wood__r,
        routes.willow_wood__spindlewood__ferndell__r,
        routes.ferndell__willow_wood__lymhurst__r,
    ],

    "martlock__thetford": [
        city_routes.martlock__blackthorn_quarry__haytor,

        routes.haytor__martlock__curlew_fen,
        routes.curlew_fen__haytor__dewleaf_fen,
        routes.dewleaf_fen__curlew_fen__fog_fen,
        routes.fog_fen__dewleaf_fen__falsestep_marsh,
        routes.falsestep_marsh__fog_fen__dusklight_fen,
        routes.dusklight_fen__falsestep_marsh__thetford,
    ],
    "martlock__fort_sterling": [
        city_routes.martlock__blackthorn_quarry__haytor,

        routes.haytor__martlock__curlew_fen,
        routes.curlew_fen__haytor__dewleaf_fen,
        routes.dewleaf_fen__curlew_fen__fog_fen,
        routes.fog_fen__dewleaf_fen__falsestep_marsh,
        routes.falsestep_marsh__fog_fen__dusklight_fen,
        routes.dusklight_fen__falsestep_marsh__thetford,

        city_routes.thetford__dusklight_fen__willowsigh_marsh,

        routes.willowsigh_marsh__thetford__sleetwater_basin,
        routes.sleetwater_basin__willowsigh_marsh__cairn_glascore,
        routes.cairn_glascore__sleetwater_basin__cairn_gorm,
        routes.cairn_gorm__cairn_glascore__cairn_fidair,
        routes.cairn_fidair__cairn_gorm__cairn_camain,
        routes.cairn_camain__cairn_fidair__fort_sterling,
    ],
    "martlock__lymhurst": [
        city_routes.martlock__haytor__blackthorn_quarry__r,

        routes.blackthorn_quarry__martlock__adrens_hill__r,
        routes.adrens_hill__blackthorn_quarry__carns_hill__r,
        routes.carns_hill__adrens_hill__felniks_hill__r,
        routes.felniks_hill__carns_hill__redstone_plain__r,
        routes.redstone_plain__felniks_hill__smoothfloor_cleft__r,
        routes.smoothfloor_cleft__redstone_plain__bridgewatch__r,

        city_routes.bridgewatch__smoothfloor_cleft__lazygrass_plain__r,

        routes.lazygrass_plain__bridgewatch__snapshaft_trough__r,
        routes.snapshaft_trough__lazygrass_plain__longshadow_plain__r,
        routes.longshadow_plain__snapshaft_trough__spindlewood__r,
        routes.spindlewood__longshadow_plain__willow_wood__r,
        routes.willow_wood__spindlewood__ferndell__r,
        routes.ferndell__willow_wood__lymhurst__r,
    ],
    "martlock__bridgewatch": [
        city_routes.martlock__haytor__blackthorn_quarry__r,

        routes.blackthorn_quarry__martlock__adrens_hill__r,
        routes.adrens_hill__blackthorn_quarry__carns_hill__r,
        routes.carns_hill__adrens_hill__felniks_hill__r,
        routes.felniks_hill__carns_hill__redstone_plain__r,
        routes.redstone_plain__felniks_hill__smoothfloor_cleft__r,
        routes.smoothfloor_cleft__redstone_plain__bridgewatch__r,
    ],

    "thetford__fort_sterling": [
        city_routes.thetford__dusklight_fen__willowsigh_marsh,

        routes.willowsigh_marsh__thetford__sleetwater_basin,
        routes.sleetwater_basin__willowsigh_marsh__cairn_glascore,
        routes.cairn_glascore__sleetwater_basin__cairn_gorm,
        routes.cairn_gorm__cairn_glascore__cairn_fidair,
        routes.cairn_fidair__cairn_gorm__cairn_camain,
        routes.cairn_camain__cairn_fidair__fort_sterling,
    ],
    "thetford__lymhurst": [
        city_routes.thetford__dusklight_fen__willowsigh_marsh,

        routes.willowsigh_marsh__thetford__sleetwater_basin,
        routes.sleetwater_basin__willowsigh_marsh__cairn_glascore,
        routes.cairn_glascore__sleetwater_basin__cairn_gorm,
        routes.cairn_gorm__cairn_glascore__cairn_fidair,
        routes.cairn_fidair__cairn_gorm__cairn_camain,
        routes.cairn_camain__cairn_fidair__fort_sterling,

        city_routes.fort_sterling__cairn_camain__mawar_gorge,

        routes.mawar_gorge__fort_sterling__pen_kerrig,
        routes.pen_kerrig__mawar_gorge__rowanwood,
        routes.rowanwood__pen_kerrig__oakcopse,
        routes.oakcopse__rowanwood__flynsdell,
        routes.flynsdell__oakcopse__birchcopse,
        routes.birchcopse__flynsdell__lymhurst,
    ],
    "thetford__bridgewatch": [
        city_routes.thetford__willowsigh_marsh__dusklight_fen__r,

        routes.dusklight_fen__thetford__falsestep_marsh__r,
        routes.falsestep_marsh__dusklight_fen__fog_fen__r,
        routes.fog_fen__falsestep_marsh__dewleaf_fen__r,
        routes.dewleaf_fen__fog_fen__curlew_fen__r,
        routes.curlew_fen__dewleaf_fen__haytor__r,
        routes.haytor__curlew_fen__martlock__r,

        city_routes.martlock__haytor__blackthorn_quarry__r,

        routes.blackthorn_quarry__martlock__adrens_hill__r,
        routes.adrens_hill__blackthorn_quarry__carns_hill__r,
        routes.carns_hill__adrens_hill__felniks_hill__r,
        routes.felniks_hill__carns_hill__redstone_plain__r,
        routes.redstone_plain__felniks_hill__smoothfloor_cleft__r,
        routes.smoothfloor_cleft__redstone_plain__bridgewatch__r,
    ],
    "thetford__martlock": [
        city_routes.thetford__willowsigh_marsh__dusklight_fen__r,

        routes.dusklight_fen__thetford__falsestep_marsh__r,
        routes.falsestep_marsh__dusklight_fen__fog_fen__r,
        routes.fog_fen__falsestep_marsh__dewleaf_fen__r,
        routes.dewleaf_fen__fog_fen__curlew_fen__r,
        routes.curlew_fen__dewleaf_fen__haytor__r,
        routes.haytor__curlew_fen__martlock__r,
    ],

    "fort_sterling__lymhurst": [
        city_routes.fort_sterling__cairn_camain__mawar_gorge,

        routes.mawar_gorge__fort_sterling__pen_kerrig,
        routes.pen_kerrig__mawar_gorge__rowanwood,
        routes.rowanwood__pen_kerrig__oakcopse,
        routes.oakcopse__rowanwood__flynsdell,
        routes.flynsdell__oakcopse__birchcopse,
        routes.birchcopse__flynsdell__lymhurst,
    ],
    "fort_sterling__bridgewatch": [
        city_routes.fort_sterling__cairn_camain__mawar_gorge,

        routes.mawar_gorge__fort_sterling__pen_kerrig,
        routes.pen_kerrig__mawar_gorge__rowanwood,
        routes.rowanwood__pen_kerrig__oakcopse,
        routes.oakcopse__rowanwood__flynsdell,
        routes.flynsdell__oakcopse__birchcopse,
        routes.birchcopse__flynsdell__lymhurst,

        city_routes.lymhurst__birchcopse__ferndell,

        routes.ferndell__lymhurst__willow_wood,
        routes.willow_wood__ferndell__spindlewood,
        routes.spindlewood__willow_wood__longshadow_plain,
        routes.longshadow_plain__spindlewood__snapshaft_trough,
        routes.snapshaft_trough__longshadow_plain__lazygrass_plain,
        routes.lazygrass_plain__snapshaft_trough__bridgewatch,
    ],
    "fort_sterling__martlock": [
        city_routes.fort_sterling__mawar_gorge__cairn_camain__r,

        routes.cairn_camain__fort_sterling__cairn_fidair__r,
        routes.cairn_fidair__cairn_camain__cairn_gorm__r,
        routes.cairn_gorm__cairn_fidair__cairn_glascore__r,
        routes.cairn_glascore__cairn_gorm__sleetwater_basin__r,
        routes.sleetwater_basin__cairn_glascore__willowsigh_marsh__r,
        routes.willowsigh_marsh__sleetwater_basin__thetford__r,

        city_routes.thetford__willowsigh_marsh__dusklight_fen__r,

        routes.dusklight_fen__thetford__falsestep_marsh__r,
        routes.falsestep_marsh__dusklight_fen__fog_fen__r,
        routes.fog_fen__falsestep_marsh__dewleaf_fen__r,
        routes.dewleaf_fen__fog_fen__curlew_fen__r,
        routes.curlew_fen__dewleaf_fen__haytor__r,
        routes.haytor__curlew_fen__martlock__r,
    ],
    "fort_sterling__thetford": [
        city_routes.fort_sterling__mawar_gorge__cairn_camain__r,

        routes.cairn_camain__fort_sterling__cairn_fidair__r,
        routes.cairn_fidair__cairn_camain__cairn_gorm__r,
        routes.cairn_gorm__cairn_fidair__cairn_glascore__r,
        routes.cairn_glascore__cairn_gorm__sleetwater_basin__r,
        routes.sleetwater_basin__cairn_glascore__willowsigh_marsh__r,
        routes.willowsigh_marsh__sleetwater_basin__thetford__r,
    ],

    "lymhurst__bridgewatch": [
        city_routes.lymhurst__birchcopse__ferndell,

        routes.ferndell__lymhurst__willow_wood,
        routes.willow_wood__ferndell__spindlewood,
        routes.spindlewood__willow_wood__longshadow_plain,
        routes.longshadow_plain__spindlewood__snapshaft_trough,
        routes.snapshaft_trough__longshadow_plain__lazygrass_plain,
        routes.lazygrass_plain__snapshaft_trough__bridgewatch,
    ],
    "lymhurst__martlock": [
        city_routes.lymhurst__birchcopse__ferndell,

        routes.ferndell__lymhurst__willow_wood,
        routes.willow_wood__ferndell__spindlewood,
        routes.spindlewood__willow_wood__longshadow_plain,
        routes.longshadow_plain__spindlewood__snapshaft_trough,
        routes.snapshaft_trough__longshadow_plain__lazygrass_plain,
        routes.lazygrass_plain__snapshaft_trough__bridgewatch,

        city_routes.bridgewatch__lazygrass_plain__smoothfloor_cleft,

        routes.smoothfloor_cleft__bridgewatch__redstone_plain,
        routes.redstone_plain__smoothfloor_cleft__felniks_hill,
        routes.felniks_hill__redstone_plain__carns_hill,
        routes.carns_hill__felniks_hill__adrens_hill,
        routes.adrens_hill__carns_hill__blackthorn_quarry,
        routes.blackthorn_quarry__adrens_hill__martlock,
    ],
    "lymhurst__thetford": [
        city_routes.lymhurst__ferndell__birchcopse__r,

        routes.birchcopse__lymhurst__flynsdell__r,
        routes.flynsdell__birchcopse__oakcopse__r,
        routes.oakcopse__flynsdell__rowanwood__r,
        routes.rowanwood__oakcopse__pen_kerrig__r,
        routes.pen_kerrig__rowanwood__mawar_gorge__r,
        routes.mawar_gorge__pen_kerrig__fort_sterling__r,

        city_routes.fort_sterling__mawar_gorge__cairn_camain__r,

        routes.cairn_camain__fort_sterling__cairn_fidair__r,
        routes.cairn_fidair__cairn_camain__cairn_gorm__r,
        routes.cairn_gorm__cairn_fidair__cairn_glascore__r,
        routes.cairn_glascore__cairn_gorm__sleetwater_basin__r,
        routes.sleetwater_basin__cairn_glascore__willowsigh_marsh__r,
        routes.willowsigh_marsh__sleetwater_basin__thetford__r,
    ],
    "lymhurst__fort_sterling": [
        city_routes.lymhurst__ferndell__birchcopse__r,

        routes.birchcopse__lymhurst__flynsdell__r,
        routes.flynsdell__birchcopse__oakcopse__r,
        routes.oakcopse__flynsdell__rowanwood__r,
        routes.rowanwood__oakcopse__pen_kerrig__r,
        routes.pen_kerrig__rowanwood__mawar_gorge__r,
        routes.mawar_gorge__pen_kerrig__fort_sterling__r,
    ],


    "bridgewatch__hornbeam_wood__treeheart_mission": [
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
    ],
})
