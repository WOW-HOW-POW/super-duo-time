// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile2 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile3 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile4 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile7 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile8 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile1 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile5 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile6 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "Map":
            case "level1":return tiles.createTilemap(hex`1000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010101010000010101010303010101010202020200000502020200000205020205020202000002020202000002020202020202020000020202020000020202020505050500000205020200000205020205050505000002020202000002020202020202020000020202020000020202020202020500000202020200000202020502020202040402020502040402020202`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
2 2 2 2 . . 2 2 2 2 2 2 2 2 2 2 
2 2 2 2 . . 2 2 2 2 . . 2 2 2 2 
2 2 2 2 . . 2 2 2 2 . . 2 2 2 2 
2 2 2 2 . . 2 2 2 2 . . 2 2 2 2 
. . . . . . 2 2 2 2 . . 2 2 2 2 
. . . . . . 2 2 2 2 . . 2 2 2 2 
2 2 2 2 . . 2 2 2 2 . . 2 2 2 2 
2 2 2 2 . . 2 2 2 2 . . 2 2 2 2 
2 2 2 2 . . 2 2 2 2 . . 2 2 2 2 
`, [myTiles.transparency16,myTiles.tile2,myTiles.tile3,myTiles.tile1,myTiles.tile5,myTiles.tile6], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
            case "Dirt":
            case "tile2":return tile2;
            case "myTile0":
            case "tile3":return tile3;
            case "Fall":
            case "tile4":return tile4;
            case "myTile3":
            case "tile7":return tile7;
            case "Triger":
            case "tile8":return tile8;
            case "myTile":
            case "tile1":return tile1;
            case "myTile1":
            case "tile5":return tile5;
            case "myTile2":
            case "tile6":return tile6;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
