# turtlebot

(Sujet)[http://sirien.metz.supelec.fr/depot/SIR/TurtleTrack/index-resp.html]

http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv

## Messages

Pour vérifier si OK
`rosmsg show cam_tracker/ArenaPosition`

## Service :

`rosservice call /camera_mod "command: 'AAA'"`

#### Modes
Les différents modes sont :
- **TRACK** : Le tracker positionne la camera sur le Turtlebot visible. Quand il y en a plus d'un, le positionnement se fait sur la cible qui engendre le déplacement minimal. Si aucun Turtlebot n'est visible, pas de mouvement.
- **SEARCH** : Le tracker cherche un Turtlebot jusqu'à ce qu'il soit détecté **TODO !**
- **SCAN** : Le tracker pouge périodiquement de sorte à couvrir la zone d'observation, indépendemment de la détection de robots

## Commandes utiles

```
catkin clean
catkin build
```
