#Nama : Bulan Fitri Dahlan
#NIM : 09021282025071
#Kelas : 4 Reguler B
# PROJECT UAS GRAFKOM

#colors = (
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#    (0, 1, 1),
#)

colors = (
    (1, 1, 1), #putih 
    (1, 1, 0), #kuning 
    (1, 0, 1), #Magenta
    (0, 1, 1), #cyan
    (1, 1, 1), #putih 
    (1, 1, 0), #kuning 
    (1, 0, 1), #Magenta
    (0, 1, 1), #cyan
    (1, 1, 1), #putih 
    (1, 1, 0), #kuning 
    (1, 0, 1), #Magenta
    (0, 1, 1), #cyan  
)

cube_verticies_vector3 = (
    (1.0000, 1.0000, 1.0000),
    (1.0000, 1.0000, -1.0000),
    (1.0000, -1.0000, 1.0000),
    (1.0000, -1.0000, -1.0000),
    (-1.0000, 1.0000, 1.0000),
    (-1.0000, 1.0000, -1.0000),
    (-1.0000, -1.0000, 1.0000),
    (-1.0000, -1.0000, -1.0000),
    )

cube_edges_vector2 = (
    (5, 7),
     (1, 5),
     (0, 1),
     (7, 6),
     (2, 3),
     (4, 5),
     (2, 6),
     (0, 2),
     (7, 3),
     (6, 4),
     (4, 0),
     (3, 1),
    )

cube_faces_vector4 = (
    (0, 4, 6, 2),
    (3, 2, 6, 7),
    (7, 6, 4, 5),
    (5, 1, 3, 7),
    (1, 0, 2, 3),
    (5, 4, 0, 1)
    )
L_verticies_vector3=(
(1.0,1.0,1.0),
(1.0,1.0,-1.0),
(1.0,-1.0,1.0),
(1.0,-1.0,-1.0),
(-1.0,1.0,1.0),
(-1.0,1.0,-1.0),
(-1.0,-1.0,1.0),
(-1.0,-1.0,-1.0),
(2.9780750274658203,1.0,1.0),
(2.9780750274658203,1.0,-1.0),
(2.9780750274658203,-1.0,1.0),
(2.9780750274658203,-1.0,-1.0),
(0.9780751466751099,1.0,1.0),
(0.9780751466751099,1.0,-1.0),
(0.9780751466751099,-1.0,1.0),
(0.9780751466751099,-1.0,-1.0),
(4.977382183074951,1.0,1.0),
(4.977382183074951,1.0,-1.0),
(4.977382183074951,-1.0,1.0),
(4.977382183074951,-1.0,-1.0),
(2.977382183074951,1.0,1.0),
(2.977382183074951,1.0,-1.0),
(2.977382183074951,-1.0,1.0),
(2.977382183074951,-1.0,-1.0),
(6.951596736907959,1.0,1.0),
(6.951596736907959,1.0,-1.0),
(6.951596736907959,-1.0,1.0),
(6.951596736907959,-1.0,-1.0),
(4.951596736907959,1.0,1.0),
(4.951596736907959,1.0,-1.0),
(4.951596736907959,-1.0,1.0),
(4.951596736907959,-1.0,-1.0),
(6.951596736907959,1.0,2.978762149810791),
(6.951596736907959,1.0,0.9787620306015015),
(6.951596736907959,-1.0,2.978762149810791),
(6.951596736907959,-1.0,0.9787620306015015),
(4.951596736907959,1.0,2.978762149810791),
(4.951596736907959,1.0,0.9787620306015015),
(4.951596736907959,-1.0,2.978762149810791),
(4.951596736907959,-1.0,0.9787620306015015),
(6.951596736907959,1.0,4.965615272521973),
(6.951596736907959,1.0,2.9656147956848145),
(6.951596736907959,-1.0,4.965615272521973),
(6.951596736907959,-1.0,2.9656147956848145),
(4.951596736907959,1.0,4.965615272521973),
(4.951596736907959,1.0,2.9656147956848145),
(4.951596736907959,-1.0,4.965615272521973),
(4.951596736907959,-1.0,2.9656147956848145),
(6.951596736907959,1.0,6.955456733703613),
(6.951596736907959,1.0,4.955455780029297),
(6.951596736907959,-1.0,6.955456733703613),
(6.951596736907959,-1.0,4.955455780029297),
(4.951596736907959,1.0,6.955456733703613),
(4.951596736907959,1.0,4.955455780029297),
(4.951596736907959,-1.0,6.955456733703613),
(4.951596736907959,-1.0,4.955455780029297),
(4.962565898895264,1.0,6.955456733703613),
(4.962565898895264,1.0,4.955455780029297),
(4.962565898895264,-1.0,6.955456733703613),
(4.962565898895264,-1.0,4.955455780029297),
(2.9625658988952637,1.0,6.955456733703613),
(2.9625658988952637,1.0,4.955455780029297),
(2.9625658988952637,-1.0,6.955456733703613),
(2.9625658988952637,-1.0,4.955455780029297),
(2.9827280044555664,1.0,6.955456733703613),
(2.9827280044555664,1.0,4.955455780029297),
(2.9827280044555664,-1.0,6.955456733703613),
(2.9827280044555664,-1.0,4.955455780029297),
(0.9827280044555664,1.0,6.955456733703613),
(0.9827280044555664,1.0,4.955455780029297),
(0.9827280044555664,-1.0,6.955456733703613),
(0.9827280044555664,-1.0,4.955455780029297),
(2.9827280044555664,1.0,4.976362228393555),
(2.9827280044555664,1.0,2.9763612747192383),
(2.9827280044555664,-1.0,4.976362228393555),
(2.9827280044555664,-1.0,2.9763612747192383),
(0.9827280044555664,1.0,4.976362228393555),
(0.9827280044555664,1.0,2.9763612747192383),
(0.9827280044555664,-1.0,4.976362228393555),
(0.9827280044555664,-1.0,2.9763612747192383),
(1.0068672895431519,1.0,4.976362228393555),
(1.0068672895431519,1.0,2.9763612747192383),
(1.0068672895431519,-1.0,4.976362228393555),
(1.0068672895431519,-1.0,2.9763612747192383),
(-0.9931327104568481,1.0,4.976362228393555),
(-0.9931327104568481,1.0,2.9763612747192383),
(-0.9931327104568481,-1.0,4.976362228393555),
(-0.9931327104568481,-1.0,2.9763612747192383),
(1.0068672895431519,1.0,2.986727714538574),
(1.0068672895431519,1.0,0.9867267608642578),
(1.0068672895431519,-1.0,2.986727714538574),
(1.0068672895431519,-1.0,0.9867267608642578),
(-0.9931327104568481,1.0,2.986727714538574),
(-0.9931327104568481,1.0,0.9867267608642578),
(-0.9931327104568481,-1.0,2.986727714538574),
(-0.9931327104568481,-1.0,0.9867267608642578),
)
L_edges_vector2=(
(5,7),
(1,5),
(0,1),
(7,6),
(2,3),
(4,5),
(2,6),
(0,2),
(7,3),
(6,4),
(4,0),
(3,1),
(13,15),
(9,13),
(8,9),
(15,14),
(10,11),
(12,13),
(10,14),
(8,10),
(15,11),
(14,12),
(12,8),
(11,9),
(21,23),
(17,21),
(16,17),
(23,22),
(18,19),
(20,21),
(18,22),
(16,18),
(23,19),
(22,20),
(20,16),
(19,17),
(29,31),
(25,29),
(24,25),
(31,30),
(26,27),
(28,29),
(26,30),
(24,26),
(31,27),
(30,28),
(28,24),
(27,25),
(37,39),
(33,37),
(32,33),
(39,38),
(34,35),
(36,37),
(34,38),
(32,34),
(39,35),
(38,36),
(36,32),
(35,33),
(45,47),
(41,45),
(40,41),
(47,46),
(42,43),
(44,45),
(42,46),
(40,42),
(47,43),
(46,44),
(44,40),
(43,41),
(53,55),
(49,53),
(48,49),
(55,54),
(50,51),
(52,53),
(50,54),
(48,50),
(55,51),
(54,52),
(52,48),
(51,49),
(61,63),
(57,61),
(56,57),
(63,62),
(58,59),
(60,61),
(58,62),
(56,58),
(63,59),
(62,60),
(60,56),
(59,57),
(69,71),
(65,69),
(64,65),
(71,70),
(66,67),
(68,69),
(66,70),
(64,66),
(71,67),
(70,68),
(68,64),
(67,65),
(77,79),
(73,77),
(72,73),
(79,78),
(74,75),
(76,77),
(74,78),
(72,74),
(79,75),
(78,76),
(76,72),
(75,73),
(85,87),
(81,85),
(80,81),
(87,86),
(82,83),
(84,85),
(82,86),
(80,82),
(87,83),
(86,84),
(84,80),
(83,81),
(93,95),
(89,93),
(88,89),
(95,94),
(90,91),
(92,93),
(90,94),
(88,90),
(95,91),
(94,92),
(92,88),
(91,89),
)
L_faces_vector4=(
(0,2,6,4),
(3,7,6,2),
(7,5,4,6),
(5,7,3,1),
(1,3,2,0),
(5,1,0,4),
(8,10,14,12),
(11,15,14,10),
(15,13,12,14),
(13,15,11,9),
(9,11,10,8),
(13,9,8,12),
(16,18,22,20),
(19,23,22,18),
(23,21,20,22),
(21,23,19,17),
(17,19,18,16),
(21,17,16,20),
(24,26,30,28),
(27,31,30,26),
(31,29,28,30),
(29,31,27,25),
(25,27,26,24),
(29,25,24,28),
(32,34,38,36),
(35,39,38,34),
(39,37,36,38),
(37,39,35,33),
(33,35,34,32),
(37,33,32,36),
(40,42,46,44),
(43,47,46,42),
(47,45,44,46),
(45,47,43,41),
(41,43,42,40),
(45,41,40,44),
(48,50,54,52),
(51,55,54,50),
(55,53,52,54),
(53,55,51,49),
(49,51,50,48),
(53,49,48,52),
(56,58,62,60),
(59,63,62,58),
(63,61,60,62),
(61,63,59,57),
(57,59,58,56),
(61,57,56,60),
(64,66,70,68),
(67,71,70,66),
(71,69,68,70),
(69,71,67,65),
(65,67,66,64),
(69,65,64,68),
(72,74,78,76),
(75,79,78,74),
(79,77,76,78),
(77,79,75,73),
(73,75,74,72),
(77,73,72,76),
(80,82,86,84),
(83,87,86,82),
(87,85,84,86),
(85,87,83,81),
(81,83,82,80),
(85,81,80,84),
(88,92,94,90),
(91,90,94,95),
(95,94,92,93),
(93,89,91,95),
(89,88,90,91),
(93,92,88,89)
)

