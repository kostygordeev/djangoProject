<html>
    <head>
        <title>App page</title>
    </head>
    <body>
        <h2>App page</h2>
        <h3>Данные для предсказания:</h3>
        <?php
            if (isset($_POST['days_num']) && isset($_POST['num_days'])) {
                $myCurl = curl_init();
                curl_setopt_array($myCurl, array(
                    CURLOPT_URL =>
                    "http://nginxserver/api?days_num=".$_POST['days_num']."&num_days=".$_POST['num_days'],
                    CURLOPT_RETURNTRANSFER => true,
                    CURLOPT_HEADER => false,
                ));
                $response = curl_exec($myCurl);
                curl_close($myCurl);

                $response_array = json_decode($response, true);
                $status = $response_array['status'];
                $message = $response_array['res'];

                echo "Статус запроса: ".$status.", сообщение: ".$message;
            }
        ?>
        <form action="index.php" method="post">
            <label for="days_num">Число дней для анализа:</label>
            <input type="text" name="days_num" id="days_num" required>
            <label for="num_days">Число дней на которой применяется анализ:</label>
            <input type="text" name="num_days" id="num_days" required>
            <input type="submit" value="RUN!">
        </form>
        <h3>Получить изображение</h3>
        <?php
            if (isset($_POST['image_name'])) {
                function generateRandomString($length = 10) {
                    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
                    $charactersLength = strlen($characters);
                    $randomString = '';
                    for ($i = 0; $i < $length; $i++) {
                        $randomString .= $characters[rand(0, $charactersLength - 1)];
                    }
                    return $randomString;
                }

                $myCurl = curl_init();
                curl_setopt_array($myCurl, array(
                    CURLOPT_URL => "http://nginxserver/img/".$_POST['image_name'],
                    CURLOPT_RETURNTRANSFER => true,
                    CURLOPT_HEADER => false,
                ));
                $response = curl_exec($myCurl);
                curl_close($myCurl);

                $response_array = json_decode($response, true);
                $base64_code = $response_array['image_base64'];
                $encoding = $response_array['encoding'];
                $image_path = "./images/".generateRandomString().".jpg";
                $image_path_full= "/var/www/html/".$image_path;

                $fp = fopen($image_path_full, "w+");
                fwrite($fp, base64_decode($base64_code));
                fclose($fp);

                echo '<img src="'.$image_path.'">';
            }
        ?>
        <form action="index.php" method="post">
            <label for="image_name">Имя изображения:</label>
            <input type="text" name="image_name" id="image_name" required>
            <input type="hidden" name="image" id ="image" value=1/>
            <input type="submit" value="GET IMAGE!">
        </form>
    </body>
</html>