;;;; ==========================================================================
;;;; SmartChef: Recipe Suggestion System in Common Lisp
;;;; Course: Fundamentals of Artificial Intelligence (FAI)
;;;; Topic: Recipe Suggestion System Using List Processing
;;;; ==========================================================================
;;;; Knowledge Representation:
;;;; Each recipe is represented as:
;;;;   (NAME (INGREDIENTS...) DIET COOKING-TIME CUISINE IMAGE-URL)
;;;;
;;;; Core List Processing Primitives Used:
;;;;   - CAR, CDR, CONS, NULL, MEMBER, MAPCAR, REMOVE-IF-NOT, SORT
;;;; ==========================================================================

(defparameter *recipes*
  '((paneer-butter-masala
     (paneer butter tomato onion cream ginger garlic garam-masala cashews kasuri-methi cumin turmeric)
     veg 30 "North Indian")

    (dal-tadka
     (lentils onion tomato garlic ginger cumin ghee chili turmeric coriander mustard-seeds)
     veg 25 "Indian Comfort")

    (vegetable-biryani
     (rice onion carrot peas potato yogurt biryani-masala mint ghee cardamom ginger garlic)
     veg 45 "Hyderabadi")

    (palak-paneer
     (spinach paneer garlic onion tomato cream cumin ginger chili butter garam-masala)
     veg 30 "North Indian")

    (chana-masala
     (chickpeas onion tomato ginger garlic coriander garam-masala cumin chili turmeric bay-leaf)
     veg 35 "Punjabi")

    (aloo-gobi
     (potato cauliflower onion tomato turmeric cumin coriander ginger garlic chili oil)
     veg 25 "North Indian")

    (masala-dosa
     (rice potato onion mustard-seeds curry-leaves turmeric chili ginger ghee oil)
     veg 20 "South Indian")

    (rajma-chawal
     (kidney-beans onion tomato ginger garlic rice cumin coriander garam-masala butter bay-leaf)
     veg 40 "North Indian")

    (butter-chicken
     (chicken butter tomato cream ginger garlic garam-masala yogurt kasuri-methi chili cashews)
     non-veg 40 "Mughlai")

    (chicken-tikka
     (chicken yogurt lemon ginger garlic chili garam-masala cumin coriander mustard-oil)
     non-veg 35 "Tandoori")

    (egg-curry
     (egg onion tomato garlic ginger turmeric coriander cumin garam-masala chili oil)
     non-veg 25 "Indian")

    (mutton-rogan-josh
     (mutton yogurt onion garlic ginger fennel cardamom chili cloves cinnamon mustard-oil)
     non-veg 60 "Kashmiri")

    (fish-curry
     (fish coconut-milk tomato onion curry-leaves mustard-seeds chili turmeric garlic oil)
     non-veg 30 "Goan Coastal")

    (pasta-aglio-e-olio
     (pasta olive-oil garlic chili parsley parmesan black-pepper sea-salt lemon)
     veg 15 "Italian")

    (margherita-pizza
     (flour tomato mozzarella basil olive-oil yeast sea-salt garlic oregano)
     veg 25 "Italian")

    (greek-salad
     (cucumber tomato olive-oil feta-cheese olives onion oregano lemon sea-salt)
     veg 10 "Mediterranean")

    (vegetable-stir-fry
     (noodles broccoli soy-sauce carrot garlic sesame-oil ginger bell-pepper chili oil)
     veg 20 "Asian")

    (minestrone-soup
     (pasta beans tomato carrot celery onion garlic olive-oil parmesan basil oregano)
     veg 30 "Italian")

    (mushroom-risotto
     (rice mushroom onion garlic vegetable-broth butter parmesan olive-oil black-pepper parsley)
     veg 35 "Italian")

    (guacamole-nachos
     (avocado lime onion tomato cilantro tortilla-chips chili garlic sea-salt)
     veg 10 "Mexican")

    (chicken-alfredo
     (pasta chicken cream butter garlic parmesan black-pepper parsley olive-oil)
     non-veg 25 "Italian-American")

    (classic-burger
     (chicken-patty bun lettuce tomato cheese onion mayo butter pickles oil)
     non-veg 20 "American")

    (grilled-salmon
     (salmon lemon olive-oil garlic black-pepper rosemary butter sea-salt parsley)
     non-veg 20 "Continental")

    (chicken-katsu-curry
     (chicken egg breadcrumbs curry-paste potato carrot rice onion oil soy-sauce)
     non-veg 40 "Japanese")))

(defparameter *substitutions*
  '((olive-oil . butter)
    (oil . butter)
    (oil . ghee)
    (tofu . paneer)
    (milk . cream)
    (yogurt . cream)
    (cheddar . parmesan)
    (cheddar . mozzarella)
    (cheese . feta-cheese)
    (mushroom . chicken)
    (chia-seeds . egg)
    (honey . sugar)
    (tomato-paste . tomato)
    (lemon . lime)))

(defun recipe-name (recipe)
  (car recipe))

(defun recipe-ingredients (recipe)
  (car (cdr recipe)))

(defun recipe-diet (recipe)
  (car (cdr (cdr recipe))))

(defun recipe-time (recipe)
  (car (cdr (cdr (cdr recipe)))))

(defun recipe-cuisine (recipe)
  (car (cdr (cdr (cdr (cdr recipe))))))

(defun get-substitutes-for (item sub-list)
  (cond
    ((null sub-list) nil)
    ((eq (cdr (car sub-list)) item)
     (cons (car (car sub-list))
           (get-substitutes-for item (cdr sub-list))))
    (t (get-substitutes-for item (cdr sub-list)))))

(defun find-first-available (candidates user-items)
  (cond
    ((null candidates) (cons nil nil))
    ((member (car candidates) user-items)
     (cons t (car candidates)))
    (t (find-first-available (cdr candidates) user-items))))

(defun has-ingredient-or-substitute-p (needed-item user-items sub-list)
  (cond
    ((member needed-item user-items)
     (cons t needed-item))
    (t
     (let ((subs (get-substitutes-for needed-item sub-list)))
       (find-first-available subs user-items)))))

(defun count-matches (user-ingredients recipe-ingredients sub-list)
  (cond
    ((null recipe-ingredients) 0)
    (t
     (let ((match-result (has-ingredient-or-substitute-p
                          (car recipe-ingredients)
                          user-ingredients
                          sub-list)))
       (if (car match-result)
           (+ 1 (count-matches user-ingredients (cdr recipe-ingredients) sub-list))
           (count-matches user-ingredients (cdr recipe-ingredients) sub-list))))))

(defun get-matched-and-missing (user-ingredients recipe-ingredients sub-list)
  (labels ((traverse (remaining-needed matched missing subs)
             (if (null remaining-needed)
                 (list matched missing subs)
                 (let* ((item (car remaining-needed))
                        (res (has-ingredient-or-substitute-p item user-ingredients sub-list))
                        (is-matched (car res))
                        (matched-as (cdr res)))
                   (cond
                     ((and is-matched (eq item matched-as))
                      (traverse (cdr remaining-needed)
                                (cons item matched)
                                missing
                                subs))
                     (is-matched
                      (traverse (cdr remaining-needed)
                                (cons matched-as matched)
                                missing
                                (cons (cons matched-as item) subs)))
                     (t
                      (traverse (cdr remaining-needed)
                                matched
                                (cons item missing)
                                subs)))))))
    (traverse recipe-ingredients nil nil nil)))

(defun match-score (match-count total-count)
  (if (zerop total-count)
      0.0
      (float (* (/ match-count total-count) 100))))

(defun filter-by-diet (recipe-list desired-diet)
  (cond
    ((or (null desired-diet) (eq desired-diet 'all))
     recipe-list)
    (t
     (remove-if-not #'(lambda (r) (eq (recipe-diet r) desired-diet))
                    recipe-list))))

(defun filter-by-time (recipe-list max-time)
  (cond
    ((or (null max-time) (<= max-time 0))
     recipe-list)
    (t
     (remove-if-not #'(lambda (r) (<= (recipe-time r) max-time))
                    recipe-list))))

(defun evaluate-recipe (recipe user-ingredients sub-list)
  (let* ((rec-ing (recipe-ingredients recipe))
         (total (length rec-ing))
         (partition (get-matched-and-missing user-ingredients rec-ing sub-list))
         (matched (first partition))
         (missing (second partition))
         (subs (third partition))
         (matches (length matched))
         (score (match-score matches total)))
    (list :recipe recipe
          :name (recipe-name recipe)
          :diet (recipe-diet recipe)
          :time (recipe-time recipe)
          :cuisine (recipe-cuisine recipe)
          :total-ingredients total
          :matched-count matches
          :score score
          :matched matched
          :missing missing
          :substitutions subs)))

(defun suggest-recipes (recipes user-ingredients &key (diet 'all) (max-time 120) (min-score 1.0))
  (let* ((diet-filtered (filter-by-diet recipes diet))
         (time-filtered (filter-by-time diet-filtered max-time))
         (evaluated (mapcar #'(lambda (r)
                                (evaluate-recipe r user-ingredients *substitutions*))
                            time-filtered))
         (qualified (remove-if-not #'(lambda (ev)
                                       (>= (getf ev :score) min-score))
                                   evaluated)))
    (sort (copy-list qualified)
          #'(lambda (a b)
              (cond
                ((> (getf a :score) (getf b :score)) t)
                ((< (getf a :score) (getf b :score)) nil)
                (t (< (getf a :time) (getf b :time))))))))

(defun symbol-to-str (sym)
  (string-downcase (symbol-name sym)))

(defun print-json-string (str stream)
  (format stream "\"~A\"" str))

(defun print-json-list (lst stream)
  (format stream "[")
  (loop for item in lst
        for i from 0
        do (progn
             (when (> i 0) (format stream ", "))
             (print-json-string (symbol-to-str item) stream)))
  (format stream "]"))

(defun print-json-subs (subs-list stream)
  (format stream "[")
  (loop for pair in subs-list
        for i from 0
        do (progn
             (when (> i 0) (format stream ", "))
             (format stream "{\"user_has\": \"~A\", \"replaces\": \"~A\"}"
                     (symbol-to-str (car pair))
                     (symbol-to-str (cdr pair)))))
  (format stream "]"))

(defun print-evaluation-json (ev stream)
  (format stream "{~%")
  (format stream "  \"id\": \"~A\",~%" (symbol-to-str (getf ev :name)))
  (format stream "  \"name\": \"~A\",~%" (substitute #\Space #\- (string-capitalize (symbol-to-str (getf ev :name)))))
  (format stream "  \"diet\": \"~A\",~%" (symbol-to-str (getf ev :diet)))
  (format stream "  \"time\": ~D,~%" (getf ev :time))
  (format stream "  \"cuisine\": \"~A\",~%" (getf ev :cuisine))
  (format stream "  \"score\": ~,2F,~%" (getf ev :score))
  (format stream "  \"matched_count\": ~D,~%" (getf ev :matched-count))
  (format stream "  \"total_count\": ~D,~%" (getf ev :total-ingredients))
  (format stream "  \"matched_ingredients\": ")
  (print-json-list (getf ev :matched) stream)
  (format stream ",~%  \"missing_ingredients\": ")
  (print-json-list (getf ev :missing) stream)
  (format stream ",~%  \"substitutions_applied\": ")
  (print-json-subs (getf ev :substitutions) stream)
  (format stream "~%}")
  t)

(defun run-cli-query (args)
  (let* ((diet-arg (if (and (>= (length args) 1) (not (string= (first args) "all")))
                       (intern (string-upcase (first args)))
                       'all))
         (time-arg (if (>= (length args) 2)
                       (parse-integer (second args) :junk-allowed t)
                       120))
         (ing-args (if (>= (length args) 3)
                       (mapcar #'(lambda (s) (intern (string-upcase s))) (nthcdr 2 args))
                       nil))
         (results (suggest-recipes *recipes* ing-args :diet diet-arg :max-time (or time-arg 120))))
    (format t "{~%")
    (format t "  \"engine\": \"Common Lisp (SBCL)\",~%")
    (format t "  \"total_evaluated\": ~D,~%" (length *recipes*))
    (format t "  \"total_matches\": ~D,~%" (length results))
    (format t "  \"results\": [~%")
    (loop for r in results
          for i from 0
          do (progn
               (when (> i 0) (format t ",~%"))
               (print-evaluation-json r *standard-output*)))
    (format t "~%  ]~%")
    (format t "}~%")))

#+sbcl
(when sb-ext:*posix-argv*
  (let ((cmd-args (cdr sb-ext:*posix-argv*)))
    (when cmd-args
      (run-cli-query cmd-args))))
