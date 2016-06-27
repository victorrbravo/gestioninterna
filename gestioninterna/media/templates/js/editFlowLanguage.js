/**
 * Set elements, fields, terminals and  properties configuration that customize
 * the language of the editor
 * */

var editFlowLanguage = {

	// Set a unique name for the language
	languageName: "editFlow",

	// inputEx fields for pipes properties
	propertiesFields: [
		// default fields (the "name" field is required by the WiringEditor):
		{
      type:       "string",
      name:       "name",
      label:      "Id",
      typeInvite: "Introduzca un Nombre"
  },
		{
      type:   "text",
      name:   "description",
      label:  "Descripción",
      cols:   25
  },
		{
      type:   "string",
      name:   "token_key",
      label:  "Key",
      cols:   25
  },
		{
      type:   "string",
      name:   "token_keysource",
      label:  "KeySource",
      cols:   25
  },
		{
      type:   "boolean",
      name:   "auto_conn",
      label:  "Conexión Automática",
      value:  true,
      cols:   25
  },
		{
      type:   "boolean",
      name:   "comments",
      label:  "Activar comentarios",
      value:  true,
      cols:   25
  },
		{
      type:   "string",
      name:   "dtd_path",
      label:  "DTD",
      cols:   25
  }
	],

	// List of node types definition
	modules:
  [
		/**
		 *	ELEMENTS
		 */
    {
			name:     "Tarea",
			category: "elements",
			container: {
      	xtype:        "TaskContainer",
      	className:    "WireIt-Container  editFlowTask",
        icon:         "/icons/task.png",
      	image:        "/icons/task.png",
        collapsible:  true,
        collapsed:    true,
        legend:       "Detalles ...",
        resizable:    false,

        /**
         *TERMINALS
         */
      	terminals:
        [
          /**
           * INPUT TERMINAL
           */
          {
            name:           "entrada",
            direction:      [-1,0],
            offsetPosition: {left: -15, top: 43},
            wireConfig:     {width: 2, borderwidth:1},
            ddConfig:       {type: "input",allowedTypes: ["output_link"]}
          },

          /**
           * OUTPUT TERMINAL
           */
          {
            name:           "salida",
            xtype:          "TaskTerminalSalida",
            editable:       false,
            direction:      [1,0],
            offsetPosition: {right: -15, top: 43},
            wireConfig:
            {
              width:        2,
              borderwidth:  1,
              xtype:        "WireIt.BezierArrowWire"
            },
            ddConfig:
            {
              type:         "output",
              allowedTypes: ["input_link"]
            },
            alwaysSrc:      true
          },

          /**
           * ASSOC TERMINAL
           */
          {
            name:           "asociativo",
            direction:      [0,-1],
            offsetPosition: {left: 85, top: -15},
            wireConfig:
            {
              width:        2,
              borderwidth:  1,
              xtype:        "WireIt.BezierWire"
            },
            ddConfig:
            {
              type:         "assoc_task",
              allowedTypes: ["assoc_var"]
            },
            alwaysSrc:      true
          }
        ],

        /**
         *FIELDS OF THE ELEMENT
         */
        fields:
        [
          //Field to set input terminal type
          {
            type:         "select",
            name:         "in",
            selectValues: ['none','or','xor','and'],
            className:    "selectIn" // Special class assigned to display
            // the field in the same line as the field selectOut
          },
          //Field to set output terminal type
          {
            type:         "select",
            name:         "out",
            selectValues: ['none','or','xor','and'],
            className:    "selectOut" // Special class assigned to display
            // the field in the same line as the field selectIn
          },
          //Field to set the id of the element
          {
            type:       "string",
            label:      "Id",
            name:       "id",
            required:   true,
            size:       15,
            typeInvite: "Introduzca Id",
            className:  "fieldclass"
          },
          //Field to set the id of the element
          {
            type:       "string",
            label:      "TexInfo",
            name:       "textualinfo",
            size:       15,
            className:  "fieldclass"
          },
          //Field to set the name or description of the element
          {
            type:         "inplaceedit",
            label:         "Título",
            name:         "content",
            editorField:  {type: "text"},
            className:    "clickEdit"
          },
          //Field to set output terminal type
          {
            type:         "select",
            label:        "Report",
            name:         "report",
            selectValues: ['no','yes'],
            className:    "fieldclass"
          },
          //Field to set output terminal type
          {
            type:         "customcolorpicker",
            label:        "color",
            name:         "color",
            showcontrols: false,
            className:    "fieldclass"
          },
        ]
      }
    },
    {
			name:     "Conexión",
			category: "elements",
			container: {
      	xtype:        "LinkContainer",
      	className:    "WireIt-Container  editFlowLink",
        icon:         "/icons/arrow.png",
      	image:        "/icons/arrow.png",
        collapsible:  true,
        collapsed:    true,
        legend:       "Detalles ...",
        resizable:    false,

        /**
         *TERMINALS
         */
      	terminals:
        [
          /**
           * INPUT TERMINAL
           */
          {
            name:           "entrada",
            direction:      [-1,0],
            offsetPosition: {left: -15, top: 23},
            wireConfig:     {width: 2, borderwidth:1},
            ddConfig:       {type: "input_link",allowedTypes: ["output"]},
            nMaxWires:      1
          },

          /**
           * OUTPUT TERMINAL
           */
          {
            name:           "salida",
            direction:      [1,0],
            offsetPosition: {right: -15, top: 23},
            wireConfig:
            {
              width:        2,
              borderwidth:  1,
              xtype:        "WireIt.BezierArrowWire",
            },
            ddConfig:
            {
              type:         "output_link",
              allowedTypes: ["input"]
            },
            alwaysSrc:      true,
            nMaxWires:      1
          }
        ],

        /**
         *FIELDS OF THE ELEMENT
         */
        fields:
        [//Field to set the query of the element
         
          //Field to set the options of the element
          {
            type:       "string",
            label:      "Options",
            name:       "options",
            className:  "fieldclass",
          },
          {
            type:       "inplaceedit",
            label:      "Query",
            name:       "query",
            value:      "true",
            required:   true,
            editorField:  {type: "text"},
            className:  "clickEditQuery"
          },
          {
            type:       "inplaceedit",
            label:      "TLink: ",
            name:       "tokenlink",
            editorField:  {type: "text"},
            className:  "clickEditQuery"
          },
          //Field to set output terminal type
          {
            type:         "customcolorpicker",
            label:        "color",
            name:         "color",
            showcontrols: false,
            className:    "fieldclass"
          },
        ]
      }
    },
    {
      name:     "Variable",
      category: "elements",
      container: {
        xtype:        "VariableContainer",
        className:    "WireIt-Container   editFlowVar",
        icon:         "/icons/variable.png",
        image:        "/icons/variable.png",
        collapsible:  true,
        collapsed:    true,
        legend:       "Detalles ...",
        resizable:    false,

        terminals:
        [
          /**
           * ASSOC TERMINAL
           */
          {
            name:           "asociativo",
            direction:      [0,-1],
            offsetPosition: {left: 60, top: -15},
            wireConfig:
            {
              width:        2,
              borderwidth:  1,
              xtype:        "WireIt.BezierWire"
            },
            ddConfig:
            {
              type:         "assoc_var",
              allowedTypes: ["assoc_task"]
            },
            nMaxWires:      1
          }
        ],

        fields:
        [
          {
            type:       "string",
            label:      "Id",
            name:       "id",
            required:   true,
            size:       15,
            typeInvite: "Introduzca Id",
            className:  "fieldclass"
          },
          {
            type:       "inplaceedit",
            label:      "TLink: ",
            name:       "tokenlink",
            editorField:  {type: "text"},
            className:  "clickEditQuery"
          },
          {
            type:       "inplaceedit",
            label:      "DocSrc:",
            name:       "documentsource",
            required:   true,
            editorField:  {type: "text"},
            className:  "clickEditQuery"
          },
          {
            type:       "string",
            label:      "RolField",
            name:       "rolfield",
            size:       15,
            className:  "fieldclass"
          },
          {
            type:       "string",
            label:      "TimeStFld",
            name:       "timestampfield",
            size:       15,
            className:  "fieldclass"
          },
          {
            label:        "Type",
            type:         "select",
            name:         "type",
            selectValues: ['sql','file','webpage'],
            className:  "fieldclass"
          },
          //Field to set output terminal type
          {
            type:         "customcolorpicker",
            label:        "color",
            name:         "color",
            showcontrols: false,
            className:    "fieldclass"
          },
        ]
      }
    },
    {
      name:     "Autofiltro",
      category: "elements",
      container: {
        xtype:        "FilterContainer",
        className:    "WireIt-Container   editFlowFilter",
        icon:         "/icons/filter2.png",
        image:        "/icons/filter2.png",
        collapsible:  true,
        collapsed:    true,
        legend:       "Detalles ...",
        resizable:    false,

        terminals:
        [
          /**
           * ASSOC TERMINAL
           */
          {
            name:           "asociativo",
            direction:      [0,-1],
            offsetPosition: {left: 60, top: -15},
            wireConfig:
            {
              width:        2,
              borderwidth:  1,
              xtype:        "WireIt.BezierWire"
            },
            ddConfig:
            {
              type:         "assoc_var",
              allowedTypes: ["assoc_task"]
            },
            alwaysSrc:      true,
            nMaxWires:      1
          },
          {
            name:           "source",
            direction:      [0,1],
            offsetPosition: {left: 60, bottom: -15},
            wireConfig:
            {
              width:        2,
              borderwidth:  1,
              xtype:        "WireIt.BezierWire"
            },
            ddConfig:
            {
              type:         "assoc_src",
              allowedTypes: ["assoc_task"]
            },
            alwaysSrc:      true,
            nMaxWires:      1
          }
        ],

        fields:
        [
          {
            type:       "string",
            label:      "Id",
            name:       "id",
            required:   true,
            typeInvite: "Introduzca Id",
            className:  "fieldclass"
          },
          {
            type:       "inplaceedit",
            label:      "Query:",
            name:       "query",
            required:   true,
            editorField:  {type: "text"},
            className:  "clickEditQuery"
          },
          {
            type:       "inplaceedit",
            label:      "TLink: ",
            name:       "tokenlink",
            editorField:  {type: "text"},
            className:  "clickEditQuery"
          },
          {
            label:        "Report",
            type:         "select",
            name:         "report",
            selectValues: ['yes','no'],
            className:  "fieldclass"
          },
          {
            label:        "Type",
            type:         "select",
            name:         "type",
            selectValues: ['split','join'],
            className:  "fieldclass"
          },
          //Field to set output terminal type
          {
            type:         "customcolorpicker",
            label:        "color",
            name:         "color",
            showcontrols: false,
            className:    "fieldclass"
          },
        ]
      }
    },


		/**
     * EVENTS
		 */

    //Start Event
		{
			name: "Condición Inicial",
			category: "events",
			container:
      {
        xtype:      "WireIt.ImageContainer",
      	 className:  "WireIt-Container WireIt-ImageContainer StartEvent",
       	icon:       "/icons/startevent.png",
      	 image:      "/images/events/startevent.png",
        close:        false,
      	terminals:
        [
          {
            name:           "salida",
            direction:      [1,0],
            offsetPosition: {left: 30, top: 17},
            wireConfig:
            {
              width:        2,
              borderwidth:  1,
              xtype:        "WireIt.BezierArrowWire"
            },
            ddConfig:       {type: "output", allowedTypes: ["input_link"]},
            alwaysSrc:      true
          }
        ]
      }
    },

    //Final Event
		{
			name: "Condición Final",
			category: "events",
			container:
      {
        xtype:"WireIt.ImageContainer",
        className: "WireIt-Container WireIt-ImageContainer EndEvent",
       	icon: "/icons/endevent.png",
        image: "/images/events/endevent.png",
        close:        false,
      	terminals:
        [
          {
            name:           "entrada",
            direction:      [-1,0],
            offsetPosition: {"left": -15, "top": 17},
            wireConfig:     {"width": 2, "borderwidth":1},
            ddConfig:       {"type": "input","allowedTypes": ["output_link"]}
          }
      	]
      }
    },
	],

	layoutOptions:
  {
    units:
    [
		 	{
        position: "top",
        height:   58,
        body:     "top"
      },
			{
        position:     "left",
        width:        210,
        resize:       true,
        body:         "left",
        gutter:       "5px",
        collapse:     true,
			  collapseSize: 25,
        header:       "EditFlow",
        scroll:       true,
        animate:      true
      },
			{
        position: "center",
        body:     "center",
        gutter:   "5px"
      },
			{
        position: "right",
        width:    250,
        resize:   true,
        body:     "right",
        gutter:   "5px",
        collapse: true,
			  collapseSize: 25, /*header: 'Properties', scroll: true,*/ animate: true
      }
		]
	}
};


